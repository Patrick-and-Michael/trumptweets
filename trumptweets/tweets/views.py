"""Views to control requests for first and last tweet ids, posting of tweet data, and new tweet requests."""
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
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
@api_view(['GET', 'POST'])
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
        new_tweet_list = request.data['statuses']
        for tweet in new_tweet_list:
            new_tweet = TweetSerializer(data=tweet)
            if new_tweet.is_valid():
                new_tweet.create(new_tweet.validated_data)
        return HttpResponse("200 OK")
