import sys
from playwright.sync_api import sync_playwright
url=sys.argv[1]
with sync_playwright() as p:
  b=p.chromium.launch();pg=b.new_page(viewport={'width':1300,'height':520});errs=[];pg.on('pageerror',lambda e:errs.append(str(e)))
  pg.goto(url);pg.wait_for_timeout(1000);pg.click('#tb')
  f=pg.frame_locator('#f');fr=[x for x in pg.frames if 'jump' in x.url][0];gr=[x for x in pg.frames if x.url.endswith(('8002/play.html','.com/play'))][0]
  pg.mouse.click(320,250)  # click iframe (menu -> start)
  pg.wait_for_timeout(300);print('after click',fr.evaluate('JSON.stringify({st,x:p.x|0})'))
  pg.keyboard.down('ArrowRight');pg.wait_for_timeout(700);pg.keyboard.press('Space');pg.wait_for_timeout(300)
  print('after keys',fr.evaluate('JSON.stringify({st,x:p.x|0,y:p.y|0})'))
  pg.screenshot(path='xtest-jump.png');pg.keyboard.up('ArrowRight')
  pg.mouse.click(960,250);pg.wait_for_timeout(200);pg.keyboard.press('Space');pg.wait_for_timeout(100);print('hop',gr.evaluate('JSON.stringify({st,v:b.v})'))
  print('errors',errs);b.close()
