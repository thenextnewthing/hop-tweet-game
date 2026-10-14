import sys
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
  b=p.chromium.launch();pg=b.new_page(viewport={'width':1300,'height':520});errs=[];pg.on('pageerror',lambda e:errs.append(str(e)))
  pg.goto(sys.argv[1]);pg.wait_for_timeout(1000);pg.click('#tb')
  fr=[x for x in pg.frames if 'jump' in x.url][0]
  pg.mouse.move(320,250);pg.mouse.down();pg.mouse.up();pg.wait_for_timeout(200)
  pg.mouse.move(600,250);pg.wait_for_timeout(700);print('run right',fr.evaluate('JSON.stringify({st,x:p.x|0,y:p.y|0,mouseOn})'))
  pg.mouse.down();pg.wait_for_timeout(120);print('jump',fr.evaluate('JSON.stringify({y:p.y|0,vy:p.vy})'));pg.wait_for_timeout(250);pg.mouse.up()
  pg.wait_for_timeout(300);pg.mouse.move(int(pg.evaluate('0')+ (fr.evaluate('(p.x-cam)*2')+5)),250);pg.wait_for_timeout(500);print('stop',fr.evaluate('JSON.stringify({x:p.x|0,vx:p.vx})'))
  pg.screenshot(path='screenshot-mouse.png');print('errors',errs);b.close()
