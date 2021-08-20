import tweepy

# Authenticate to Twitter
auth = tweepy.OAuthHandler("zUo5D5ITJ8KFxAwrKGVqSsIQ0", 
"Cc8eNi7iPRxI8rGfWicVTfIOvjRZJ4xaCAURj3m8aYDPXCxU04")
auth.set_access_token("1139464201464946688-qp8WxWt3TE9LzoD8rNvoHWdXajOhDX",
 "nAoTHGQw5Xiaj8x8B5Y72G8MpXmMAc4qLSnhe2gB12BKZ")

# Create API object
api = tweepy.API(auth)

# Create a tweet
api.update_status("Hello Tweepy /n. Thie tweet is sent via the twitter API. ")