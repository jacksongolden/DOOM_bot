import config
import tweepy
import genius_api

# -------------------- TWITTER API SETUP ------------------
api_key = config.twitter_api_key
api_key_secret = config.twitter_api_key_secret

access_token = config.twitter_access_token
access_token_secret = config.twitter_access_token_secret

bearer_token = config.twitter_bearer_token

# Twitter requires oAuth2 to access its API:
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
# ---------------------------------------------------------


# ~~~~~~~~~~~~~~~~~~~~ Main Script ~~~~~~~~~~~~~~~~~~~~~~~~
# # "Hello world" example
# api.update_status('Hello world')

# Example to post random quote from quote_api.py
# def tweet_quote():
#     tweet = quote_api.get_quote()
#     status = api.update_status(tweet)
#     print(status.id)
#
# tweet_quote()

# Post random MF DOOM lyric from genius_api.py
def post_tweet():
    tweet_info = genius_api.get_tweet_info()
    status = api.update_status(tweet_info)
    print(status.id)


post_tweet()
