import tweepy
from textblob import TextBlob

# Unique code from Twitter
access_token = "44199763-QbzzHMshq9X4iOew1ZIy1ByPWBTmulba6jG5gpWQA"
access_token_secret = "CHrzNqxCAtuUu7Vk2p9x4Yo9gAQrpEgeMDeFFeWDJdtmL"
consumer_key = "r4jg39kOcc8cmpjEQANJVL7W7"
consumer_secret = "UlN5CZoS7LKQojpfxKkA2aRXUjpU2t23gD0I74kFgOEGFgRbS6"

# Boilerplate code here
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)
#Now we can Create Tweets, Delete Tweets, and Find Twitter Users

public_tweets = api.search('"Gilmore Girls" @netflix')

for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)


#polarity -- measures how positive or negative
#subjectivity -- measures how factual.

#1 Sentiment Analysis - Understand and Extracting Feelings from Data
