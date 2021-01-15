import requests
import tweepy
import quote_api

# -------------------- TWITTER API SETUP ------------------
api_key = "anXvsgomMdt3rrAipwZjTSnVT"
api_key_secret = "xeGfriyE6WafI96XiKjo3VBZUrJZStCyIMpVzUG7RgACDllsfF"

access_token = "1349899085155885058-o16M4QH44X7dxWcGiDotZs7IxXeJVX"
access_token_secret = "ddVVXJZXfiMzBltRAsbcnJn1OwSnoTLc84UrLzsErUN6o"

bearer_token = \
    "AAAAAAAAAAAAAAAAAAAAAM4uLwEAAAAAUb1BMLZxQ20rRIp3CSPUMmaIH6g%3DVmLyLVA1kcGKMmoA6915zTYEA7R11uRPapct6WJuvHgrVKsrT9"
# Twitter requires oAuth2 to access its API:
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
# ---------------------------------------------------------


# ~~~~~~~~~~~~~~~~~~~~ Main Script ~~~~~~~~~~~~~~~~~~~~~~~~
# # "Hello world" example
# api.update_status('Hello world')

# Example to post random quote from quote_api.py
def tweet_quote():
    tweet = quote_api.get_quote()
    status = api.update_status(tweet)
    print(status.id)

tweet_quote()
