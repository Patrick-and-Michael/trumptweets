from django.db.models import (
    CharField,
    DateField,
    IntegerField,
    Model,
)


class Tweet(Model):
    raw_text = CharField(max_length=512)     # Tweepy.models.status.text
    author_name = CharField(max_length=256)  # Tweepy.models.status.author.name
    author_id = IntegerField()  # Tweepy.models.status.author.id
    created_at = DateField()    # Tweepy.models.created_at (a datetime.datetime object)
    tweet_id = IntegerField()         # Tweepy.models.status.id
