# -*- coding: utf-8 -*-
import sys
import tweepy
from datetime import datetime
#from textwrap import TextWrapper
#import MySQLdb as mdb
#import socket
#socket.setdefaulttimeout(timeout)
 
authcredz = open(".tpass").read().split("\n")
VIP = [x.split("\t") for x in open("resultsOfScrape.txt").read().split("\n")]
ids = [x[3] for x in VIP]

#files = [open(VIP[i][2],"w") for i in range(len(VIP))]

 
auth1 = tweepy.OAuthHandler(authcredz[0], authcredz[1])
auth1.set_access_token(authcredz[2], authcredz[3])
f = open("pelicansbeak3.txt", 'w')


 
class StreamListener(tweepy.StreamListener):
    #conn = mdb.connect('localhost', 'nelson','nelson','testdb')
    def on_status(self, status):
		try:
			original_tweet = (status.text + '\t')
			print status.user.screen_name,status.text
			encoded_tweet = original_tweet.encode('UTF-8')
			f.write(str(status.user.screen_name)+"|"+str(status.user.id)+"|"+str(datetime.now())+"|"+status.text+"|"+str(status.retweet_count)+"\n")#+"|"+str(status.author.id)+"|"+str(status.retweet_count)+"\n"+str(status.author.screen_name)
			#cursor = self.conn.cursor()
			#cursor.execute('INSERT INTO tweets (text, date) VALUES (%s, NOW())' ,(status.text))
		except KeyboardInterrupt:
			raise
			return False
		except Exception,  e:
			print("ah damn")
			#log.write("hell if I know")
			return True
		except SSLError as e:
			log.write("Error establishing the connection")
			return True
		except IncompleteRead as r:
			log.write("Error with HTTP connection")
			# Catch any unicode errors while printing to console
			# and just ignore them to avoid breaking application.
		return True

l = StreamListener()
streamer = tweepy.Stream(auth=auth1, listener=l, timeout=None,secure=True )
print('streamer initialized')
setTerms = ['cheese']
#sample to sample all public tweets
streamer.filter(ids)
print('filter initialized and running')
