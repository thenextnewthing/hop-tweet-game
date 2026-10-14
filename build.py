import json,base64
r=lambda f:open(f).read();b=lambda f:base64.b64encode(open(f,'rb').read()).decode()
H={'/play':r('play.html'),'/x':r('x.html'),'/':r('x.html'),'/jump/play':r('jump/play.html'),'/jump/x':r('jump/x.html'),'/jump':r('jump/x.html'),
   '/join/play':r('join/play.html'),'/join/x':r('join/x.html'),'/join':r('join/x.html')}
P={'/card.png':['image/png',b('card.png')],'/jump/card.png':['image/png',b('jump/card.png')],'/join/card.png':['image/png',b('join/card.png')],
   '/join/guide.pdf':['application/pdf',b('join/guide.pdf')]}
open('worker.js','w').write("const H="+json.dumps(H)+";const P="+json.dumps(P)+";\n"+r('worker_src.js'))
