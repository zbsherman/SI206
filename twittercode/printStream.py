import tweepy
import json

# Unique code from Twitter
access_token = "44199763-QbzzHMshq9X4iOew1ZIy1ByPWBTmulba6jG5gpWQA"
access_token_secret = "CHrzNqxCAtuUu7Vk2p9x4Yo9gAQrpEgeMDeFFeWDJdtmL"
consumer_key = "r4jg39kOcc8cmpjEQANJVL7W7"
consumer_secret = "UlN5CZoS7LKQojpfxKkA2aRXUjpU2t23gD0I74kFgOEGFgRbS6"

# Boilerplate code here
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)
def process_or_store(tweet):
	print(tweet.get('user').get('screen_name'))
	print(tweet.get('text').encode('unicode_escape'))
	print(tweet.get('created_at'))

for status in tweepy.Cursor(api.home_timeline).items(10):
    # Process a single status
    process_or_store(status._json) 


for tweet in tweepy.Cursor(api.user_timeline).items():
    process_or_store(tweet._json)


