const fs=require('fs'),vm=require('vm'),assert=require('assert'),path=require('path');
const root=path.resolve(process.argv[2]||'.'),L=require(path.join(root,'docs/logic.js'));
const context={window:{}};vm.createContext(context);vm.runInContext(fs.readFileSync(path.join(root,'docs/data.js'),'utf8'),context);const D=context.window.PROJECT_DATA;
let total=0;const close=(a,b)=>{assert.ok(Math.abs(a-b)<1e-9,`${a} != ${b}`);total++};
const fp=path.join(root,'tests/fixtures.json');if(fs.existsSync(fp)){for(const f of JSON.parse(fs.readFileSync(fp))){if(D.model.mean)L.crop(f.input,D.model).forEach((v,i)=>close(v,f.expected[i]));else if(D.model.vocab)L.textModel(f.input,D.model).prob.forEach((v,i)=>close(v,f.expected[i]));else close(L.housing(f.input,D.model).value,f.expected)}}
assert.throws(()=>L.crop([NaN],{}));assert.deepEqual(L.fit([0,1,2],[1,3,5]),{slope:2,intercept:1});assert.throws(()=>L.fit([1,1,1],[1,2,3]));
assert.equal(L.simulate(30,10,100).accepted,30);assert.equal(L.simulate(30,10,400).accepted,15);assert.equal(L.simulate(30,10,400).dropped,15);
assert.equal(L.marketCSV('date,close\n2025-01-03,3\n2025-01-01,1\n2025-01-02,2')[0].value,1);
assert.throws(()=>L.marketCSV('date,close\n2025-02-30,3\n2025-01-01,1\n2025-01-02,2'));
assert.throws(()=>L.marketCSV('date,close\n2025-01-01,3\n2025-01-01,1\n2025-01-02,2'));
assert.throws(()=>L.parseCSV('"unclosed'));
// Lightweight DOM harness checks initialization and event wiring, not layout.
const html=fs.readFileSync(path.join(root,'docs/index.html'),'utf8'),nodes=new Map();
function add(id,attrs=''){const n={value:(attrs.match(/value="([^"]*)"/)||[])[1]||'',textContent:'',_html:'',events:{},addEventListener(k,f){this.events[k]=f},focus(){},click(){}};Object.defineProperty(n,'innerHTML',{get(){return this._html},set(v){this._html=v;for(const m of v.matchAll(/<[^>]*\bid="([^"]+)"[^>]*>/g))add(m[1],m[0])}});nodes.set(id,n);return n}
for(const m of html.matchAll(/<[^>]*\bid="([^"]+)"[^>]*>/g))add(m[1],m[0]);const doc={getElementById:id=>{assert.ok(nodes.has(id),'Missing element '+id);return nodes.get(id)},createElement:()=>({click(){}})};
const ui={window:{PROJECT_DATA:D},document:doc,Lab:L,console,Blob,URL,setTimeout};vm.createContext(ui);vm.runInContext(fs.readFileSync(path.join(root,'docs/app.js'),'utf8'),ui);assert.ok(nodes.get('dataset-content').innerHTML.length>200);
if(nodes.has('controls')&&nodes.get('controls').events.submit)nodes.get('controls').events.submit({preventDefault(){}});
if(nodes.has('reset'))nodes.get('reset').onclick?.();
if(nodes.has('clear')){nodes.get('clear').onclick();assert.equal(nodes.get('prediction').textContent,'Enter a message');nodes.get('example').value='2';nodes.get('example').onchange();assert.equal(nodes.get('prediction').textContent,'Unknown vocabulary')}
console.log(path.basename(root)+': PASS; '+total+' numeric parity checks; input validation, initialization and controls checked.');
