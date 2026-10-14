import json,base64
h=json.dumps(open('site/play.html').read());xh=json.dumps(open('site/x.html').read());png=base64.b64encode(open('site/card.png','rb').read()).decode()
open('worker.js','w').write(f"""const PLAY={h};const X={xh};const PNG="{png}";
const hdr={{'content-security-policy':"frame-ancestors 'self' https://x.com https://*.x.com https://twitter.com https://*.twitter.com",'cache-control':'public, max-age=300'}};
export default {{async fetch(r){{const p=new URL(r.url).pathname;
if(p==='/card.png'){{const b=Uint8Array.from(atob(PNG),c=>c.charCodeAt(0));return new Response(b,{{headers:{{...hdr,'content-type':'image/png'}}}})}}
if(p==='/play'||p==='/play.html')return new Response(PLAY,{{headers:{{...hdr,'content-type':'text/html; charset=utf-8'}}}});
return new Response(X,{{headers:{{...hdr,'content-type':'text/html; charset=utf-8'}}}})}}}};
""")
