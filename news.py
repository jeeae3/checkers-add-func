import tweepy
import pandas as pd
import requests
import json
from requests_oauthlib import OAuth1

class TwitterNews:
    def __init__(self):
        self.consumer_key = "bmFRsptBkVwKxwruFMZEW7Eis"
        self.consumer_secret = "EwxBUW7llwWY2vfAdca1oqiloeZb9lYXp6lLVWjZuCNUs19VeS"
        self.access_token = "1981466952603197440-MVPvpLDB6p0zuXFdjsGuwGjYrJ4iBU"
        self.access_token_secret = "7rb6htt2JgIpDKgGDfcp8vscfM4dz8OamLIDBPiPXvhQ0"
        self.bearer_token = "AAAAAAAAAAAAAAAAAAAAAKD24wEAAAAA%2FrJwH4FD37ZzDTNOk08gvEAwGvw%3DtKk77DDjFjGZbtc8wCzZHiIEp5jDBUWq5UMrhpb8qorelnQTMt"
        
        # Setup authentication
        self.auth_tweepy = tweepy.OAuth1UserHandler(
            self.consumer_key, self.consumer_secret,
            self.access_token, self.access_token_secret
        )
        self.auth_requests = OAuth1(self.consumer_key, self.consumer_secret, self.access_token, self.access_token_secret)
        
        # Initialize API clients
        self.api = tweepy.API(self.auth_tweepy, wait_on_rate_limit=True)
        self.client = tweepy.Client(bearer_token=self.bearer_token)
        
        # Get user data
        self.headers = {"Authorization": f"Bearer {self.bearer_token}"}
        self.user_response = requests.get(
            "https://api.x.com/2/users/by/username/TempleAlerts", headers=self.headers
        )
        
        #print(f"\nResponse status: {self.user_response.status_code}")
        #print(f"\nResponse: {self.user_response.text}")
        
        if self.user_response.status_code == 200:
            self.user_data = self.user_response.json()
            self.user_id = self.user_data['data']['id']
            self.user_name = self.user_data['data']['name']
            
            # Get tweets
            self.user_tweets = self.client.get_users_tweets(id=self.user_id, max_results=10)
            
            # Print results
            #print(f"User ID: {self.user_id}")
            #print(f"User Name: {self.user_name}")
            #print(f"Number of tweets retrieved: {len(self.user_tweets.data) if self.user_tweets.data else 0}")
            if self.user_tweets.data:
                print(f"Most recent tweet: {self.user_tweets.data[0].text}")
                #print(f"Oldest tweet: {self.user_tweets.data[-1].text}")
        else:
            print("Failed to get user data")
            self.user_data = None
            self.user_id = None
            self.user_name = None
            self.user_tweets = None

# Create instance to run the code
news = TwitterNews()


