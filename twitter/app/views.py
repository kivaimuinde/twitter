from re import template
import re
import requests
from django.shortcuts import render
from django.http import Http404, response
from django.shortcuts import redirect
#needed to access the Twitter API
'''
tweepy is used to create new tweets
'''
import tweepy

'''
twint is needed to scrap data from twitter. Unlike tweepy, 
it is unbound to twitter rules and can s
crap way large number of tweets
'''

import twint

# Authenticate to Twitter
auth = tweepy.OAuthHandler("zUo5D5ITJ8KFxAwrKGVqSsIQ0", 
"Cc8eNi7iPRxI8rGfWicVTfIOvjRZJ4xaCAURj3m8aYDPXCxU04")
auth.set_access_token("1139464201464946688-qp8WxWt3TE9LzoD8rNvoHWdXajOhDX",
 "nAoTHGQw5Xiaj8x8B5Y72G8MpXmMAc4qLSnhe2gB12BKZ")

# Create API object
api = tweepy.API(auth)


def home(request):
    timeline = api.home_timeline()
    template_name='home.html'
    context= {
        'timeline':timeline,
        'title':'Welcome to Twitter Bot & Scrapper'
     }
    return render(request, context=context, template_name=template_name)

#user profile

def profile(request, user_id):
    template_name="profile.html"
    try:
        u_profile=api.get_user(user_id)
    except:
        raise Http404("Record not Found")

    tweets=api.user_timeline(screen_name=api.get_user(user_id), 
                           # 200 is the maximum allowed count
                           count=200,
                           include_rts = False,
                           # Necessary to keep full_text 
                           # otherwise only the first 140 words are extracted
                           tweet_mode = 'extended'
                           )
    context={
        'user':u_profile,
        'tweets':tweets,
        'title':u_profile
    }
    return render(request, template_name, context)


#user timeline
def user_timeline(request, user_id):
    template_name="user_timeline.html"
    try:
        u_profile=api.get_user(user_id, count=100, page=25)
    except:
        raise Http404("Record not Found")
    context={
        'user':u_profile,
        'title':'User Time Line'
    }
    return render(request, template_name, context)


#create new tweet
def create_tweet(request):
    if request.method=='GET':
        template_name='tweet.html'
        context={
            'title': 'Create New Tweet'
        }
        return render(request, template_name, context)
    else:
        tweet_message=request.POST.get('tweet')
        api.update_status(tweet_message)
        return redirect('index')