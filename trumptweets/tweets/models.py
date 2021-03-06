from django.db.models import (
    CharField,
    DateTimeField,
    BigIntegerField,
    Model,
)


class Tweet(Model):
    raw_text = CharField(max_length=512)     # Tweepy.models.status.text
    author_name = CharField(max_length=256)  # Tweepy.models.status.author.name
    author_id = BigIntegerField()  # Tweepy.models.status.author.id
    created_at = DateTimeField()    # Tweepy.models.status.created_at (a datetime.datetime object)
    tweet_id = BigIntegerField()   # Tweepy.models.status.id

    def __str__(self):
        return self
