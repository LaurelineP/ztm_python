import os
from dotenv import load_dotenv, dotenv_values
import tweepy
import requests
import configparser
import sys
from __utils.index import print_non_dunder

sys.path.append('../../__utils')


load_dotenv()
API_KEY = os.getenv('TW_API_KEY')
API_SECRET_KEY = os.getenv('TW_API_SECRET_KEY')
CUSTOMER_KEY = os.getenv('TW_CUSTOMER_KEY')
CUSTOMER_SECRET_KEY = os.getenv('TW_CUSTOMER_SECRET_KEY')
ACCESS_TOKEN = os.getenv('TW_ACCESS_TOKEN')
ACCESS_SECRET_TOKEN = os.getenv('TW_ACCESS_SECRET_TOKEN')
BEARER_TOKEN = os.getenv('TW_BEARER_TOKEN')


# auth = tweepy.OAuthHandler(
# # consumer_key, consumer_secret, access_token, access_token_secret
#    API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_SECRET_TOKEN
# )
# auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
# auth.set_access_token(ACCEqSS_TOKEN, ACCESS_SECRET_TOKEN)
#
# api = tweepy.API(auth)



# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)

# print(api.get_user())
def set_account():
	_auth = tweepy.OAuthHandler( CUSTOMER_KEY, CUSTOMER_SECRET_KEY )
	_auth.set_access_token(ACCESS_TOKEN,ACCESS_SECRET_TOKEN)
	return _auth

def create_api(auth):
	try:
		api = tweepy.API(auth)
		return api
	except ValueError as error:
		print('h', error)


def set_account1():
	client = tweepy.Client(
		bearer_token=BEARER_TOKEN,
		consumer_key=CUSTOMER_KEY,
		consumer_secret=CUSTOMER_SECRET_KEY,
		access_token=ACCESS_TOKEN,
		access_token_secret=ACCESS_SECRET_TOKEN
	)
	return client


def display_about_me(client: tweepy.Client):
	me = client.get_me(user_fields=['public_metrics'])
	print(f"My name: {me.data.name}")

#
auth = set_account()
api = create_api(auth)
# api.update_status('Helloww')
# auth = set_account()
# print_non_dunder(api)
try:
	print(api.get_friends())
except ValueError as e:
	print(e)
# display_about_me(client)

################################################
# https://medium.com/mlearning-ai/how-to-get-tweets-by-python-and-twitter-api-2022-a440c635c3ac
# auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
# auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET_TOKEN)
#
# api = tweepy.API(auth)
#
# public_tweets = api.home_timeline()