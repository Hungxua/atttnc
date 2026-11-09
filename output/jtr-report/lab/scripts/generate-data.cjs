const fs=require('fs'),path=require('path'),crypto=require('crypto');
const bcrypt=require('bcryptjs');
if(!process.argv[2]) throw Error('Pass a NEW output lab directory: node generate-data.cjs NEW_LAB_DIR');
const root=path.resolve(process.argv[2]);
if(fs.existsSync(path.join(root,'data/checksums.json'))) throw Error('Refusing to replace frozen data');
function write(p,s){fs.mkdirSync(path.dirname(path.join(root,p)),{recursive:true});fs.writeFileSync(path.join(root,p),s,'utf8');}
const left='amber apple autumn bamboo beach blue bright cedar cherry cloud coral crystal dawn delta dream eagle earth ember fern field forest frost garden gentle golden green happy hazel honey island ivory jade lake lemon light lotus maple meadow moon morning mountain ocean olive orange orchid pearl pine quiet rain red river robin rose ruby silver sky snow solar spring star stone summer sunny swift tiger valley violet warm wave white wild willow wind winter yellow'.split(' ');
const right='bird bloom brook cloud coast creek dawn deer dove dream fern field fire fish flower fox gate grove hill home lake leaf light lion moon nest oak path peak pine pond rain reed rock rose sand seed sky song star stone sun tree vale view walk wave wind wing wood'.split(' ');
const words=[];for(const a of left)for(const b of right){words.push(a+b);if(words.length===1000)break;} 
const wl=[...new Set(words)].slice(0,1000);if(wl.length!==1000)throw Error('wordlist size');
const rules=[':', 'c', 'c$2$0$2$6$!', '$1$2$3'];
write('data/wordlist.txt',wl.join('\n')+'\n');
write('configs/lab-rules.conf','[List.Rules:Lab]\n'+rules.join('\n')+'\n');
const candidates=[...new Set([...wl,...wl.map(x=>x[0].toUpperCase()+x.slice(1)),...wl.map(x=>x[0].toUpperCase()+x.slice(1)+'2026!'),...wl.map(x=>x+'123')])];
write('data/candidates.txt',candidates.join('\n')+'\n');
const rec=[];
function add(g,p,method){rec.push({id:`${g}_${String(rec.filter(x=>x.group===g).length+1).padStart(2,'0')}`,group:g,password:p,length:p.length,method});}
for(let i=0;i<20;i++)add('G1',wl[i*43],'wordlist index i*43');
for(let i=0;i<20;i++){let b=wl[21+i*43];add('G2',b[0].toUpperCase()+b.slice(1)+'2026!','capitalize + 2026!; wordlist index 21+i*43');}
for(let i=0;i<20;i++){let p=String.fromCharCode(97+crypto.randomInt(26),97+crypto.randomInt(26))+String(crypto.randomInt(10000)).padStart(4,'0');add('G3',p,'crypto.randomInt, 2 lowercase ASCII + 4 digits');}
const alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*';
for(let i=0;i<20;i++){let p='';for(let j=0;j<12+i%5;j++)p+=alphabet[crypto.randomInt(alphabet.length)];add('G4',p,'crypto.randomInt; length 12..16; alphabet 70');}
for(let i=0;i<20;i++)add('G5',Array.from({length:3},()=>left[crypto.randomInt(left.length)]).join('-'),'3 randomly selected words, hyphen separated');
if(new Set(rec.map(x=>x.password)).size!==100)throw Error('duplicate password');
write('ground-truth/passwords.json',JSON.stringify(rec,null,2));
write('data/manifest.csv','id,group,length,generation_method\n'+rec.map(x=>`${x.id},${x.group},${x.length},"${x.method}"`).join('\n')+'\n');
write('data/sha256.txt',rec.map(x=>crypto.createHash('sha256').update(x.password).digest('hex')).join('\n')+'\n');
const map=[];
for(const cost of [10,12]){
 console.log('Generating bcrypt',cost);
 const rows=rec.map((x,i)=>{const h=bcrypt.hashSync(x.password,cost);if(!bcrypt.compareSync(x.password,h))throw Error('verification');map.push({id:x.id,cost,hash:h});if(i%20===0)console.log(cost,i);return h;});
 write(`data/bcrypt${cost}.txt`,rows.join('\n')+'\n');
}
write('ground-truth/hash-map.json',JSON.stringify(map,null,2));
const control='CONTROL-ABSENT-9vQ7#x!';if(candidates.includes(control))throw Error('control overlaps');
write('data/control-sha256.txt',crypto.createHash('sha256').update(control).digest('hex')+'\n');
for(const cost of [10,12])write(`data/control-bcrypt${cost}.txt`,bcrypt.hashSync(control,cost)+'\n');
const single=Array.from({length:8},(_,i)=>{let u=['alice','bruno','carol','david','elena','frank','grace','henry'][i];let h=crypto.createHash('sha256').update(u).digest('hex');return `${u}:${h}:100${i}:100${i}:${u} Lab:/home/${u}:/bin/bash`;});
write('data/single.txt',single.join('\n')+'\n');
const files=['data/wordlist.txt','data/candidates.txt','data/manifest.csv','data/sha256.txt','data/bcrypt10.txt','data/bcrypt12.txt','data/single.txt','data/control-sha256.txt','data/control-bcrypt10.txt','data/control-bcrypt12.txt','ground-truth/passwords.json','ground-truth/hash-map.json','configs/lab-rules.conf'];
write('data/checksums.json',JSON.stringify(Object.fromEntries(files.map(p=>[p,crypto.createHash('sha256').update(fs.readFileSync(path.join(root,p))).digest('hex')])),null,2));
write('environment/dataset-generation.json',JSON.stringify({created:new Date().toISOString(),node:process.version,bcryptjs:require('bcryptjs/package.json').version,wordlist:wl.length,candidates:candidates.length,records:rec.length,note:'Synthetic controlled data; no real accounts. Original files, not a seed, are the reproducibility authority.'},null,2));
console.log('Dataset verified',rec.length,candidates.length);
