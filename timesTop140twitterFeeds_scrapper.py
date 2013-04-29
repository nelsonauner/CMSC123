import urllib
import urllib2
import string
import sys
import re

from bs4 import BeautifulSoup


user_agent = 'Mozilla/5 (Solaris 10) Gecko'
headers = { 'User-Agent' : user_agent }

todo = open("timeurls.txt","r").read().split("\n")
output = open("twitterout.txt","a")

def getSite(url):
    webpage = urllib.urlopen(url).read()
    return webpage

results = []
for url in todo:
	x = getSite(url)
	# example is: r = re.findall('def(.*?)end', x)

	r = re.findall('\(@(.*?)\)',x)
	if r == []:
		r = re.findall('https://twitter\.com/(.*?)/status',x)
		r = r[0]
	r = r[0]
	if r == []:
		output.write(url+"|"+"UNKNOWN | UNKNOWN\n")
		break
	
	twitterurl =  getSite("https://twitter.com/"+r)
	twitterid = re.findall('data-user-id=\"(.*?)\">',twitterurl)[4]
	output.write(url+"|"+r+"|"+twitterid+"\n")