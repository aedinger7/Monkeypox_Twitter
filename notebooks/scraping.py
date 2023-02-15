from tweepy.auth import OAuth2BearerHandler
from tweepy import Cursor
from tweepy import API
import tweepy
import os
import json
import bz2
import config

BASE_PATH = "../data/dataverse_files"

# set BEARER_TOKEN to your twitter access token
BEARER_TOKEN = config.Bearer_Token

dates=[]
tweet_ids=[]

for file in os.listdir(BASE_PATH):
    if file.endswith(".txt"):
        ids = open(BASE_PATH + '/'+ file, 'r')
        count = 0
        date = file[:7]
        # Strips the newline character
        for line in ids.readlines():
            count += 1
            tweet_id=line.strip()
#             print("Date: {}\tLine{}: {}".format(date, count, tweet_id))
            dates.append(date)
            tweet_ids.append(tweet_id)
            
print(len(tweet_ids))

auth = OAuth2BearerHandler(BEARER_TOKEN)
client = API(auth, wait_on_rate_limit=True)

sfile = '../data/monkeypox_tweets_081222.bz2'

tweets = []

interval = 100

print_interval = 100

for i in range(len(tweet_ids)//interval + 1):
    data = client.lookup_statuses(tweet_ids[i*interval : (i+1)*interval], tweet_mode="extended")
    tweets += [i._json for i in data]
    if len(tweets) > print_interval:
        print(len(tweets),"tweets retrieved")
        print_interval += 10000

        # Compress JSON as BZ2 and save
        with bz2.open(sfile, "w") as f:
            f.write(json.dumps(tweets).encode())
            
        # Open bz2 and read JSON to test
        with bz2.BZ2File(sfile, 'r') as f:
            test_read = []
            for line in f.readlines():
                tweets = json.loads(line.decode().strip("\n"))
                test_read = test_read + tweets

        print(len(test_read), "tweets saved and read")

# Compress JSON as BZ2 and save
with bz2.open(sfile, "w") as f:
    f.write(json.dumps(tweets).encode())
    
# Open bz2 and read JSON to test
with bz2.BZ2File(sfile, 'r') as f:
    test_read = []
    for line in f.readlines():
        tweets = json.loads(line.decode().strip("\n"))
        test_read = test_read + tweets

print(len(test_read), "tweets saved and read")

print("Finished scraping:", len(tweets), "tweets retrieved")






