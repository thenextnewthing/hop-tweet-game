const hdr={'cache-control':'public, max-age=300'};
const RL=new Map();// best-effort per-isolate rate limit
function limited(ip){const now=Date.now(),w=10*60e3,a=(RL.get(ip)||[]).filter(t=>now-t<w);a.push(now);RL.set(ip,a);if(RL.size>5000)RL.clear();return a.length>5}
const J=(o,s=200)=>new Response(JSON.stringify(o),{status:s,headers:{'content-type':'application/json','cache-control':'no-store'}});
async function subscribe(req,env){
  let d;try{d=await req.json()}catch{return J({ok:false,message:'Bad request.'},400)}
  if(d.company)return J({ok:false,message:'Something went wrong.'},400);
  const email=String(d.email||'').trim().toLowerCase();
  if(email.length>254||!/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(email))return J({ok:false,message:'Please enter a valid email.'},400);
  const ip=req.headers.get('cf-connecting-ip')||'?';if(limited(ip))return J({ok:false,message:'Too many tries. Please wait a few minutes.'},429);
  if(!env.BEEHIIV_API_KEY||!env.BEEHIIV_PUBLICATION_ID){console.error('subscribe: beehiiv not configured (BEEHIIV_API_KEY / BEEHIIV_PUBLICATION_ID missing)');
    return J({ok:false,code:'not_configured',message:"Signups aren't open just yet. Please check back soon."},503)}
  const r=await fetch(`https://api.beehiiv.com/v2/publications/${env.BEEHIIV_PUBLICATION_ID}/subscriptions`,{method:'POST',
    headers:{authorization:`Bearer ${env.BEEHIIV_API_KEY}`,'content-type':'application/json'},
    body:JSON.stringify({email,reactivate_existing:false,send_welcome_email:true,utm_source:'x',utm_medium:'tweet-card',referring_site:'x.com'})});
  if(r.ok)return J({ok:true});
  console.error('subscribe: beehiiv error',r.status,(await r.text()).slice(0,500));
  return J({ok:false,message:"We couldn't sign you up right now. Please try again in a minute."},502)}
export default {async fetch(req,env){let p=new URL(req.url).pathname.replace(/\.html$/,'');if(p.length>1)p=p.replace(/\/$/,'');
  if(p==='/join/api/subscribe'){if(req.method!=='POST')return J({ok:false,message:'POST only'},405);try{return await subscribe(req,env)}catch(e){console.error('subscribe crash',e);return J({ok:false,message:'Something went wrong.'},500)}}
  if(P[p]){const[t,d]=P[p];return new Response(Uint8Array.from(atob(d),c=>c.charCodeAt(0)),{headers:{...hdr,'content-type':t}})}
  if(H[p])return new Response(H[p],{headers:{...hdr,'content-type':'text/html; charset=utf-8'}});
  return new Response('Not found',{status:404})}};
