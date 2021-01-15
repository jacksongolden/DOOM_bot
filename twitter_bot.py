import config
import tweepy
import genius_api

# -------------------- TWITTER API SETUP ------------------
api_key = config.api_key
api_key_secret = config.api_key_secret

access_token = config.access_token
access_token_secret = config.access_token_secret

bearer_token = config.bearer_token

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
def tweet_lyric():
    tweet = genius_api.make_tweet()
    status = api.update_status(tweet)
    print(status.id)


tweet_lyric()
