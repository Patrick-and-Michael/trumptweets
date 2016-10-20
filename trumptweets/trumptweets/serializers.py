from rest_framework import serializers
from .models import Tweet


class TweetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tweet
        fields = (
            'raw_text',
            'author_name',
            'author_id',
            'tweet_id',
            'created_at',
            )
