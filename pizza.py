import config
import tweepy
from twilio.rest import Client
import re
from datetime import datetime

# setup 
consumer_key = config.TWITTER_CONFIG['consumer_key']
consumer_secret = config.TWITTER_CONFIG['consumer_secret']
access_token = config.TWITTER_CONFIG['access_token']
access_token_secret = config.TWITTER_CONFIG['access_token_secret']
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
twitterAPI = tweepy.API(auth)
contacts = config.CONTACTS

# returns tweet containing today's free names, if it exists 
def getFreeNamesTweet(tweets): 
    today = datetime.today().date()
    for tweet in tweets: 
        date_of_tweet = tweet.created_at.date()
        x = re.search(".*free.*name", tweet.text)
        if (x is not None and (today == date_of_tweet)): 
            # the free names for the day have been tweeted! 
            return tweet

    # if the free name tweet has not been posted yet, return false 
    return False 

# returns the lucky soul who is getting free pizza on this fateful day 
def matchNames(tweet): 
    text = tweet.text
    for name in contacts.keys():
        # iterate over each word in the tweet to avoid false name matches
        for word in text.split():
            if name == word: 
                # woohoo free pizza, baby! 
                return ({ "name": name, "number": contacts[name] })
    # no free pizza for you :( 
    return False

# free pizza notification 
def sendText(lucky): 
    account_sid = config.TWILIO_CONFIG['account_sid']
    auth_token  = config.TWILIO_CONFIG['auth_token']

    client = Client(account_sid, auth_token)
    text = "Yay {}! You get free pizza today :)".format(lucky['name'])
    message = client.messages.create(
        to=lucky['number'], 
        from_=config.TWILIO_CONFIG['sender'],
        body=text)


def main(): 
    # get latest tweets from stobies and locate today's free pizza names 
    stobies_tweets = twitterAPI.user_timeline("@Stobiespizza")
    tweet = getFreeNamesTweet(stobies_tweets)
    if tweet: 
        free = matchNames(tweet)
        if free: 
            # somebody gets free pizza today! let them know :) 
            sendText(free)


main()