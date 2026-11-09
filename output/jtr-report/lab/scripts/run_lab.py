"""Run only the supplied synthetic lab data. Python 3 stdlib; no network."""
import argparse, csv, hashlib, json, os, pathlib, platform, re, subprocess, time
from datetime import datetime, timezone

LAB=pathlib.Path(__file__).resolve().parents[1]
J=pathlib.Path(os.environ.get('JTR_BIN',str(LAB/'tools/john-1.9.0-jumbo-1-win64/run/john.exe'))).resolve()
HC=pathlib.Path(os.environ.get('HASHCAT_BIN',str(LAB/'tools/hashcat-8.0.0/hashcat.exe'))).resolve()
ENV=dict(os.environ,OMP_NUM_THREADS='4',OMP_WAIT_POLICY='PASSIVE')
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def check():
    for p,h in json.loads((LAB/'data/checksums.json').read_text()).items():
        assert sha(LAB/p)==h, f'Changed frozen input: {p}'
def capture(cmd,name):
    p=subprocess.run([str(x) for x in cmd],cwd=J.parent,env=ENV,capture_output=True,timeout=90)
    s=(p.stdout+p.stderr).decode('utf8','replace')
    (LAB/'environment'/name).write_text(s,encoding='utf8');return s
def setup():
    check()
    # Keep upstream config unchanged. Explicit include resolves default settings.
    cfg=f'.include "{(J.parent/"john.conf").as_posix()}"\n'+(LAB/'configs/lab-rules.conf').read_text()
    (LAB/'configs/experiment.conf').write_text(cfg,encoding='ascii')
    capture([J,'--list=build-info'],'john-build.txt')
    capture([J,'--list=formats'],'john-formats.txt')
    capture([J,'--list=inc-modes'],'john-incremental-modes.txt')
    capture([J,'--format=raw-sha256','--test=0'],'selftest-sha256.txt')
    capture([J,'--format=bcrypt','--test=0'],'selftest-bcrypt.txt')
    if HC.exists(): capture([HC,'-I'],'hashcat-devices.txt')
    host={'platform':platform.platform(),'processor':platform.processor(),'logical_cpus':os.cpu_count(),'omp_threads':4,'python':platform.python_version(),'measured_environment':'Windows native; not a Linux VM','john_sha256':sha(J),'hashcat_sha256':sha(HC) if HC.exists() else None}
    (LAB/'environment/host.json').write_text(json.dumps(host,indent=2),encoding='utf8')
def run(code,fmt,ds,mode,rep,seconds,phase='formal',tool='john'):
    check();rid=f'{code}_r{rep}';out=LAB/'results'/phase/rid
    if out.exists(): raise RuntimeError(f'Existing run preserved: {out}')
    out.mkdir(parents=True)
    pot=out/'result.pot'; target=LAB/'data'/ds
    if tool=='john':
        cmd=[str(J),f'--config={(LAB/"configs/experiment.conf").as_posix()}',f'--format={fmt}',*mode,f'--max-run-time={seconds}',f'--session={(out/"session").as_posix()}',f'--pot={pot.as_posix()}',target.as_posix()]
        cwd=J.parent
    else:
        dtype=os.environ.get('HASHCAT_DEVICE_TYPE','1')
        backend=['--backend-ignore-cuda','-d','1'] if dtype=='2' else []
        cmd=[str(HC),'-m','1400','-a','0','-D',dtype,*backend,'--runtime',str(seconds),'--potfile-path',str(pot),'--session',rid,'--restore-disable','--status','--status-timer','10',str(target),str(LAB/'data/candidates.txt')]
        cwd=HC.parent
    start=time.perf_counter();began=datetime.now(timezone.utc).isoformat()
    with (out/'terminal.log').open('wb') as log:
        p=subprocess.Popen(cmd,cwd=cwd,env=ENV,stdout=log,stderr=subprocess.STDOUT,creationflags=getattr(subprocess,'CREATE_NO_WINDOW',0))
        snapshots=[]
        while p.poll() is None:
            elapsed=time.perf_counter()-start
            snapshots.append({'elapsed_s':round(elapsed,3),'pot_lines_observed':len(pot.read_text(errors='replace').splitlines()) if pot.exists() else 0})
            if elapsed>seconds+120: p.kill();raise RuntimeError('Process exceeded grace period')
            try: p.wait(timeout=.1)
            except subprocess.TimeoutExpired: pass
    wall=time.perf_counter()-start
    log=(out/'terminal.log').read_text(encoding='utf8',errors='replace')
    truth=json.loads((LAB/'ground-truth/passwords.json').read_text())
    plains=set()
    if pot.exists():
        for line in pot.read_text(encoding='utf8',errors='replace').splitlines():
            if ':' in line: plains.add(line.split(':',1)[1])
    recovered=[x for x in truth if x['password'] in plains] if not ds.startswith('control-') and ds!='single.txt' else []
    stop='time_limit' if 'max run-time reached' in log or re.search(r'Status\.*:\s*Aborted \(Runtime\)',log) else 'completed'
    if 'No password hashes loaded' in log or 'Unknown option' in log or 'Invalid options' in log or (tool=='hashcat' and p.returncode not in [0,1,4]):stop='error'
    if p.returncode!=0 and tool=='john' and not (p.returncode==1 and stop=='time_limit'):stop='error'
    result={'run_id':rid,'code':code,'phase':phase,'tool':tool,'format':fmt,'dataset':ds,'budget_s':seconds,'wall_time_s':round(wall,4),'exit_code':p.returncode,'stop_reason':stop,'started_utc':began,'dataset_sha256':sha(target),'candidates_sha256':sha(LAB/'data/candidates.txt'),'recovered':len(plains) if ds=='single.txt' else len(recovered),'groups':{g:sum(x['group']==g for x in recovered) for g in ['G1','G2','G3','G4','G5']},'pot_lines':len(plains),'command':cmd,'log_path':str((out/'terminal.log').relative_to(LAB)),'speed_lines':[l for l in log.splitlines() if re.search(r'\d[.\d]*[kKMGT]?[pcC]/s|Speed\.#',l)]}
    (out/'result.json').write_text(json.dumps(result,indent=2),encoding='utf8')
    (out/'pot-observations.json').write_text(json.dumps(snapshots),encoding='utf8')
    print(rid,stop,result['recovered'],result['groups'],f'{wall:.2f}s',flush=True)
    if stop=='error': print(log[-3500:],flush=True)
    return result
def suite(phase,budget):
    wl=f'--wordlist={(LAB/"data/wordlist.txt").as_posix()}'
    ca=f'--wordlist={(LAB/"data/candidates.txt").as_posix()}'
    cases=[('A1','raw-sha256','sha256.txt',[wl]),('A2','raw-sha256','sha256.txt',[wl,'--rules=Lab']),('A3','raw-sha256','sha256.txt',['--mask=?l?l?d?d?d?d']),('A4','raw-sha256','sha256.txt',['--incremental=LowerNum','--min-length=1','--max-length=6']),('B1','raw-sha256','sha256.txt',[ca]),('B2','bcrypt','bcrypt10.txt',[ca]),('B3','bcrypt','bcrypt12.txt',[ca]),('D1','raw-sha256','control-sha256.txt',[ca]),('D2','bcrypt','control-bcrypt10.txt',[ca]),('D3','bcrypt','control-bcrypt12.txt',[ca])]
    for rep in range(1,2 if phase=='pilot' else 4):
        for code,fmt,ds,mode in cases[rep-1:]+cases[:rep-1]:
            run(code,fmt,ds,mode,rep,budget,phase)
    run('A5','raw-sha256','sha256.txt',['--mask=?d?d?d?d?d?d'],1,min(30,budget),phase)
    run('A6','raw-sha256','single.txt',['--single'],1,min(30,budget),phase)
    if HC.exists():
        for rep in range(1,2 if phase=='pilot' else 4):run('C_H','raw-sha256','sha256.txt',[],rep,budget,phase,'hashcat')
    rows=[json.loads(p.read_text()) for p in sorted((LAB/'results'/phase).glob('*/result.json'))]
    fields=['run_id','tool','format','dataset','budget_s','wall_time_s','recovered','stop_reason','exit_code']
    with (LAB/'results'/f'{phase}-summary.csv').open('w',newline='',encoding='utf-8-sig') as f:
        w=csv.DictWriter(f,fields,extrasaction='ignore');w.writeheader();w.writerows(rows)
if __name__=='__main__':
    a=argparse.ArgumentParser();a.add_argument('--phase',choices=['pilot','formal','setup','gpu'],default='pilot');a.add_argument('--budget',type=int,default=5);args=a.parse_args();setup()
    if args.phase=='gpu':
        os.environ['HASHCAT_DEVICE_TYPE']='2'
        for rep in range(1,4):run('C_G','raw-sha256','sha256.txt',[],rep,args.budget,'formal','hashcat')
    elif args.phase!='setup':suite(args.phase,args.budget)
