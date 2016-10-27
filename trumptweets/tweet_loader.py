import os
import tweepy

from nltk import TweetTokenizer

from tweets.models import Tweet

consumer_key = os.environ.get("CONSUMER_KEY")
consumer_secret = os.environ.get("CONSUMER_SECRET")
access_token = os.environ.get("ACCESS_TOKEN")
access_token_secret = os.environ.get("ACCESS_TOKEN_SECRET")

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

trump = api.get_user("realDonaldTrump")

try:
    since_id = Tweet.objects.all().order_by('tweet_id').first().tweet_id
except AttributeError:
    since_id = 1

recent_tweets = tweepy.Cursor(api.user_timeline,
                              id=trump.id,
                              since_id=since_id).items(20)
