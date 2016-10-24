"""Use twitter API to get Donald's tweets."""
from itertools import chain
from nltk import TweetTokenizer
import math, os, random, tweepy

consumer_key = os.environ.get("CONSUMER_KEY")
consumer_secret = os.environ.get("CONSUMER_SECRET")
access_token = os.environ.get("ACCESS_TOKEN")
access_token_secret = os.environ.get("ACCESS_TOKEN_SECRET")

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

trump = api.get_user("realDonaldTrump")

recent_tweets = tweepy.Cursor(api.user_timeline, id=trump.id).items(20)

tweet_list = [x for x in recent_tweets]

tweet_texts = [x.text for x in tweet_list]

tokenizer = TweetTokenizer()

token_list = [tokenizer.tokenize(item) for item in tweet_texts]

avg_words = len(list(chain.from_iterable(token_list))) / len(token_list)

target_length = math.ceil(avg_words)

def get_first_word(token_list):
    return random.choice([token[0] for token in token_list if len(token) > 2])

def make_bigrams(token_list):
    bigrams = {}
    for s in token_list:
        for i, token in enumerate(s):
            try:
                bigrams.get(token).append(s[i+1]) if bigrams.get(token) else bigrams.setdefault(token, [s[i + 1]])
            except IndexError:
                bigrams.get(token).append("[END]") if bigrams.get(token) else bigrams.setdefault(token, ["[END]"])
    return bigrams



def get_next_word(prev_word, bigrams):
    return random.choice(bigrams[prev_word])

def make_tweet():
    first_word = get_first_word(token_list)
    bigrams = make_bigrams(token_list)
    tweet = [first_word]
    next_word = get_next_word(first_word, bigrams)
    """Future feature: tweet should fall within 2.5 standard devs of avg_words."""
    while next_word != "[END]" and len(tweet) < avg_words * 3:
        tweet.append(next_word)
        next_word = get_next_word(next_word, bigrams)
    if tweet[-1] == "[END]":
        tweet.pop()
    return " ".join(tweet)

if __name__ == "__main__":
    fake_tweet = make_tweet()
    print(fake_tweet)
