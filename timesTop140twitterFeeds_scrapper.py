##import necessary libraries (some of these are not actually necessary)
import urllib
import urllib2
import string
import sys
import re
from bs4 import BeautifulSoup

#Tell the computer who we are.
user_agent = 'Mozilla/5 (Solaris 10) Gecko'
#I don't know what this one means
headers = { 'User-Agent' : user_agent }

#todo is a list of urls to scrape
todo = open("timeurls.txt","r").read().split("\n")
#file to write our results to
output = open("twitterout.txt","a")

#function to return the html of a url
def getSite(url):
    webpage = urllib.urlopen(url).read()
    return webpage

	
#main loop to go through each url, look for @ and write to a file. 
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
	#use the @---- data to open their profile on twitter and scrape it, look for data-user-id=... and scrape the id number. 
	twitterurl =  getSite("https://twitter.com/"+r)
	twitterid = re.findall('data-user-id=\"(.*?)\">',twitterurl)[4]
	output.write(url+"|"+r+"|"+twitterid+"\n")