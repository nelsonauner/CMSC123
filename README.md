CMSC123 Project 
Nelson Auner
nauner [at] uchicago [dot] edu
==============
Introduction
==============
I scrapped a list of Time Magazine's "Top 140 twitter feeds of 2013", sorted by category (e.g. politics, etc)
Then I scrapped their twitter feed user ids, wrote a script to capture all of their tweets, and ran it on my own computer. 
I was not able to get the script working on AWS, despite having successfully put twitter-scrapers on AWS previously. 
A problem was that the twitter module (tweepy) returned all tweets that were loosly connected with the "Top 140 feeds", and returned them all together.
I was not able to sort these tweets to which of the 140 they should be attributed to. 
However, I did return some interesting data sets. bostonsample.txt is a large sample of tweets over the course of the Boston Marathon bombings and subsequent manhunt. 
TwitterResult -ALL and -VIP have twitter scraps for a representative sample of twitter users (ALL) and for the top 140 (VIP).








==============
Progress Report
==============
Step 1) Created twitter developer account, familiarized myself with tweepy
Step 2) Practice with Tweepy/twitter scrapping: streamed all tweets mentioning "Boston" during the 24-hour manhunt. See attached file
Step 3) Found a possible data set: Time Magazine's "Top 140 twitter feeds of 2013", sorted by category. Available at http://techland.time.com/2013/03/25/140-best-twitter-feeds-of-2013/slide/all/
Step 4) Wrote a scrapper to access Time's website (above) and scrape twitter handlers for the list. Integrated it with a second scrapper, that, using the twitter handle, went to that handle's twitter page and scraped the numeric twitter ID #, necessary for using tweepy. Edited the results to include Time Magazine's category. See resultsofScrape.txt
Step 5) Write a script that scrapes everything said by the 140 top files. Also, a feed that tracks general twitter analysis
Step 6) Set up above script on AWS

---current status is here ---

Step 7) After collecting data, analyze with nltk



