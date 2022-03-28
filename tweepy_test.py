import tweepy

from credentials import BEARER_TOKEN
from credentials import API_KEY
from credentials import API_KEY_SECRET
from credentials import ACCESS_TOKEN
from credentials import ACCESS_TOKEN_SECRET

client = tweepy.Client(bearer_token=BEARER_TOKEN,
                       consumer_key=API_KEY,
                       consumer_secret=API_KEY_SECRET,
                       access_token=ACCESS_TOKEN,
                       access_token_secret=ACCESS_TOKEN_SECRET)

try:
    user = client.get_me()
    print(user)
except tweepy.Unauthorized:
    print("There may have been an issue with the consumer_key or consumer_secret you entered.")
