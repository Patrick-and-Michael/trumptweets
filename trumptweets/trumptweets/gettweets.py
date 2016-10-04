"""Use twitter API to get Donald's tweets."""
import os
import tweepy

consumer_key = os.environ.get("CONSUMER_KEY")
consumer_secret = os.environ.get("CONSUMER_SECRET")
access_token = os.environ.get("ACCESS_TOKEN")
access_token_secret = os.environ.get("ACCESS_TOKEN_SECRET")

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

trump = api.get_user("realDonaldTrump")

recenttweets = tweepy.Cursor(api.user_timeline, id=trump.id).items(20)
