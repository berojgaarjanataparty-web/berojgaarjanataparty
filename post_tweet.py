import tweepy
import os
import random

tweets = [
    """🚨 NEET UG Paper Leak — Demand Justice!\n\n1,50,000+ people demand removal of Education Minister Dharmendra Pradhan.\n\nJoin the campaign!\n\n#NEETScam #NEETPaperLeak #RemoveDharmendraPradhan #StudentsDeserveJustice""",

    """📢 Students of India deserve better!\n\nThe NEET UG paper leak is a betrayal of millions of hardworking students.\n\nSign the petition NOW!\n\n#NEETScam #CJP #Justice #RemoveDharmendraPradhan""",

    """✊ 1.5 Lakh+ voices cannot be ignored!\n\nCockroach Janata Party demands accountability for the NEET UG paper leak.\n\nSpread the word!\n\n#NEETPaperLeak #NEETScam #StudentsFirst""",
]

client = tweepy.Client(
    consumer_key=os.environ["API_KEY"],
    consumer_secret=os.environ["API_SECRET"],
    access_token=os.environ["ACCESS_TOKEN"],
    access_token_secret=os.environ["ACCESS_TOKEN_SECRET"]
)

tweet = random.choice(tweets)
client.create_tweet(text=tweet)
print("Tweet posted!")
