import sys,asyncio
from playwright.sync_api import sync_playwright
url,out,w,h,play=sys.argv[1],sys.argv[2],int(sys.argv[3]),int(sys.argv[4]),sys.argv[5]=='1'
with sync_playwright() as p:
  b=p.chromium.launch();pg=b.new_page(viewport={'width':w,'height':h});pg.goto(url);pg.wait_for_timeout(600)
  if play:
    for i in range(14): pg.keyboard.press('Space');pg.wait_for_timeout(330)
  pg.screenshot(path=out);b.close()
