import os
import tweepy
from tqdm import tqdm
import json
import csv

creds = json.load(open('creds.json'))

auth = tweepy.OAuth1UserHandler(creds['api_key'], creds['api_key_secret'])
auth.set_access_token(creds['access_token'], creds['access_token_secret'])

api = tweepy.API(auth, wait_on_rate_limit=True)


def scrape_hashtag(hashtag, path, n_items):
    with open(path, 'w', encoding='utf-8', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(['text', 'source', 'source_url', 'date', 'id_str'])
        for tweet in tweepy.Cursor(api.search_tweets, q=hashtag + ' -filter:retweets', lang='en').items(n_items):
            msg = [tweet.text, tweet.source, tweet.source_url, tweet.created_at, str(tweet.id_str)]
            csvwriter.writerow(msg)
    return


if __name__ == '__main__':
    hashtags = ["#cats", "#dogs", "#pets"]
    for hashtag in tqdm(hashtags):
        max_tweets = 10000
        scrape_hashtag(hashtag, hashtag[1:] + '.csv', max_tweets)

