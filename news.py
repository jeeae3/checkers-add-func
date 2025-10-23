import tweepy
import pandas as pd
import requests
import json
from requests_oauthlib import OAuth1

consumer_key = "bmFRsptBkVwKxwruFMZEW7Eis"
consumer_secret = "EwxBUW7llwWY2vfAdca1oqiloeZb9lYXp6lLVWjZuCNUs19VeS"
access_token = "1981466952603197440-MVPvpLDB6p0zuXFdjsGuwGjYrJ4iBU"
access_token_secret = "7rb6htt2JgIpDKgGDfcp8vscfM4dz8OamLIDBPiPXvhQ0"
bearer_token = "AAAAAAAAAAAAAAAAAAAAAKD24wEAAAAA%2FrJwH4FD37ZzDTNOk08gvEAwGvw%3DtKk77DDjFjGZbtc8wCzZHiIEp5jDBUWq5UMrhpb8qorelnQTMt"

# Setup authentication
auth_tweepy = tweepy.OAuth1UserHandler(
    consumer_key, consumer_secret,
    access_token, access_token_secret
)
auth_requests = OAuth1(consumer_key, consumer_secret, access_token, access_token_secret)

# Initialize API clients
api = tweepy.API(auth_tweepy, wait_on_rate_limit=True)
client = tweepy.Client(bearer_token=bearer_token)

# Get user data
headers = {"Authorization": f"Bearer {bearer_token}"}
user_response = requests.get(
    "https://api.x.com/2/users/by/username/TempleAlerts", headers=headers
)

if user_response.status_code == 200:
    user_data = user_response.json()
    user_id = user_data['data']['id']
    user_name = user_data['data']['name']
    
    # Get tweets
    user_tweets = client.get_users_tweets(id=user_id, max_results=10)
    
    if user_tweets.data:
        print(f"Most recent tweet: {user_tweets.data[0].text}")
else:
    print("Failed to get user data")
    user_data = None
    user_id = None
    user_name = None
    user_tweets = None


