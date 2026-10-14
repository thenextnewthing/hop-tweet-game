import json,base64
r=lambda f:open(f).read();b=lambda f:base64.b64encode(open(f,'rb').read()).decode()
H={'/play':r('play.html'),'/x':r('x.html'),'/':r('x.html'),'/jump/play':r('jump/play.html'),'/jump/x':r('jump/x.html'),'/jump':r('jump/x.html')}
P={'/card.png':b('card.png'),'/jump/card.png':b('jump/card.png')}
open('worker.js','w').write("const H="+json.dumps(H)+";const P="+json.dumps(P)+""";
const hdr={'cache-control':'public, max-age=300'};
export default {async fetch(r){let p=new URL(r.url).pathname.replace(/\\.html$/,'');if(p.length>1)p=p.replace(/\\/$/,'');
if(P[p])return new Response(Uint8Array.from(atob(P[p]),c=>c.charCodeAt(0)),{headers:{...hdr,'content-type':'image/png'}});
if(H[p])return new Response(H[p],{headers:{...hdr,'content-type':'text/html; charset=utf-8'}});
return new Response('Not found',{status:404})}};
""")
