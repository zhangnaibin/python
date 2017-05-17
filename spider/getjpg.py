import urllib
import re

def get_page(url):
	page=urllib.urlopen(url)
	html=page.read()
	return html

def get_image(page):
	reg=r'src="(.+?\.jpg)" size='
	imgrex=re.compile(reg)
	imglist=re.findall(imgrex,page)
	x=0
	for img in imglist:
		urllib.urlretrieve(img, '%s.jpg'%x)		
		x+=1

html=get_page('https://tieba.baidu.com/p/5115387470')
get_image(html)
