import tweepy

# Unique code from Twitter
access_token = ""
access_token_secret = ""
consumer_key = ""
consumer_secret = ""

# Boilerplate code here
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api = tweepy.API(auth)
#Now we can Create Tweets, Delete Tweets, and Find Twitter Users

public_tweets = api.search('UMSI')


for tweet in public_tweets:
	print(tweet.text)
	
#Learn more about Search
#https://dev.twitter.com/rest/public/search

