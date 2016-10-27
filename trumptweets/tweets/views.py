"""Views to control requests for first and last tweet ids, posting of tweet data, and new tweet requests."""
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Tweet
from .serializers import TweetSerializer


class JSONResponse(HttpResponse):
    """An HttpResponse that renders content to JSON."""

    def __init__(self, data, **kwargs):
        """An init method."""
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
def tweet_loader(request):
    """Get first and last tweet id from database, or add tweets."""
    if request.method == 'GET':
        try:
            tweets = Tweet.objects.all().order_by('tweet_id')
            data = {'oldest': tweets.first().tweet_id, 'newest': tweets.last().tweet_id}
        except AttributeError:
            data = {'oldest': 0, 'newest': 0}

        # json = JSONRenderer.render(data)
        return JSONResponse(data)

    if request.method == 'POST':
        new_tweet_list = request.data
        for tweet in new_tweet_list:
            TweetSerializer(tweet).create()
