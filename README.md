CMSC123 Project 
Nelson Auner
=======

Step 1) Created twitter developer account, familiarized myself with tweepy
Step 2) Practice with Tweepy/twitter scrapping: streamed all tweets mentioning "Boston" during the 24-hour manhunt. See attached file
Step 3) Found a possible data set: Time Magazine's "Top 140 twitter feeds of 2013", sorted by category. Available at http://techland.time.com/2013/03/25/140-best-twitter-feeds-of-2013/slide/all/
Step 4) Wrote a scrapper to access Time's website (above) and scrape twitter handlers for the list. Integrated it with a second scrapper, that, using the twitter handle, went to that handle's twitter page and scraped the numeric twitter ID #, necessary for using tweepy. Edited the results to include Time Magazine's category. See resultsofScrape.txt

---current status is here ---

Step 5) Write a script that scrapes everything said by the 140 top files. Also, a feed that tracks general twitter analysis
Step 6) Set up above script on AWS
Step 7) After collecting data, analyze with nltk
