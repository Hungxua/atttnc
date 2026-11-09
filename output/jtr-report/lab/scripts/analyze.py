"""Verify frozen synthetic inputs and pot results, aggregate independent runs."""
import collections,csv,hashlib,json,pathlib,re,statistics,sys
LAB=pathlib.Path(__file__).resolve().parents[1]
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def load(p):return json.loads(p.read_text(encoding='utf-8-sig'))
for p,h in load(LAB/'data/checksums.json').items():assert digest(LAB/p)==h,p
truth=load(LAB/'ground-truth/passwords.json')
assert len(truth)==100 and len({x['password'] for x in truth})==100
assert collections.Counter(x['group'] for x in truth)==dict.fromkeys(['G1','G2','G3','G4','G5'],20)
hashmap=load(LAB/'ground-truth/hash-map.json')
assert len({x['hash'][7:29] for x in hashmap})==200,'Salt uniqueness'
plain_by_id={x['id']:x['password'] for x in truth}
known={hashlib.sha256(x['password'].encode()).hexdigest():x['password'] for x in truth}
known.update({x['hash']:plain_by_id[x['id']] for x in hashmap})
for user in ['alice','bruno','carol','david','elena','frank','grace','henry']:
    known[hashlib.sha256(user.encode()).hexdigest()]=user
rows=[]
for p in sorted((LAB/'results/formal').glob('*/result.json')):
    r=load(p);log=(p.parent/'terminal.log').read_text(encoding='utf8',errors='replace')
    if r['tool']=='hashcat' and re.search(r'Status\.*:\s*Exhausted',log):
        r['stop_reason']='completed'
        p.write_text(json.dumps(r,indent=2),encoding='utf8')
    pot=p.parent/'result.pot';n=0
    if pot.exists():
        for line in pot.read_text(encoding='utf8',errors='replace').splitlines():
            h,v=line.split(':',1);h=h.removeprefix('$SHA256$')
            assert h in known and known[h]==v,f'Invalid recovery: {p} {h}'
            n+=1
    assert n==r['pot_lines'],f'count mismatch {p}'
    assert r['dataset_sha256']==digest(LAB/'data'/r['dataset'])
    speeds=re.findall(r'([0-9]+(?:\.[0-9]+)?)([kKMGT]?)p/s',log)
    r['last_p_s']=float(speeds[-1][0])*{'':1,'k':1e3,'K':1e3,'M':1e6,'G':1e9,'T':1e12}[speeds[-1][1]] if speeds else None
    rows.append(r)
summary={}
for code in sorted({r['code'] for r in rows}):
    group=[r for r in rows if r['code']==code]
    good=[r for r in group if r['stop_reason']!='error']
    def stats(k):
        v=[r[k] for r in good if r.get(k) is not None]
        return {'median':statistics.median(v),'min':min(v),'max':max(v)} if v else None
    summary[code]={'runs':len(group),'successful_runs':len(good),'recovered':stats('recovered'),'wall_time_s':stats('wall_time_s'),'p_s':stats('last_p_s'),'groups':{g:statistics.median([r['groups'][g] for r in good]) for g in ['G1','G2','G3','G4','G5']} if good else None,'stop_reasons':collections.Counter(r['stop_reason'] for r in group)}
for code in ['A1','A2','A3','A4','B1','B2','B3','D1','D2','D3']:
    assert summary.get(code,{}).get('successful_runs')==3,f'Need 3 valid runs: {code}'
assert summary['A1']['recovered']['median']==20
assert summary['A2']['recovered']['median']==40
assert summary['A3']['recovered']['median']==20
assert summary['A5']['recovered']['median']==0
assert summary['A6']['recovered']['median']==8
(LAB/'results/analysis.json').write_text(json.dumps({'summary':summary,'runs':rows},indent=2),encoding='utf8')
fields=['run_id','tool','format','dataset','budget_s','wall_time_s','recovered','last_p_s','stop_reason','exit_code']
with (LAB/'results/all-runs.csv').open('w',encoding='utf-8-sig',newline='') as f:
    w=csv.DictWriter(f,fields,extrasaction='ignore');w.writeheader();w.writerows(rows)
(LAB/'results/verification.json').write_text(json.dumps({'frozen_inputs':'PASS','records':100,'groups':5,'unique_bcrypt_salts':200,'pot_hash_plaintext_pairs':'PASS','core_3_repeats':'PASS','formal_run_count':len(rows),'note':'Backend failures retained, not counted as successful performance measurements.'},indent=2),encoding='utf8')
print(json.dumps(summary,indent=2))
