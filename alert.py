import tweepy
import config

consumer_key = config.API_KEY
consumer_secret = config.API_SECRET
access_token = config.ACCESS_TOKEN
access_token_secret = config.ACCESS_TOKEN_SECRET
bearer_token = config.BEARER_TOKEN

# https://docs.tweepy.org/en/stable/authentication.html#tweepy.OAuthHandler
# classtweepy.OAuthHandler(consumer_key, consumer_secret, access_token=None, access_token_secret=None, callback=None)

def client():
   client = tweepy.Client(bearer_token, consumer_key, consumer_secret, access_token, access_token_secret)
   return client
def auth():
   auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
   return auth
def create_tweet(entry):
   api = tweepy.API(auth())
   client().create_tweet(text = entry)