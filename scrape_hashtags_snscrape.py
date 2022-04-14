import os
import csv
import snscrape.modules.twitter as sntwitter
import pandas as pd
from tqdm import tqdm


def scrape_hashtag(hashtag, path, n_items):
    tweets = []
    i = 0
    with open(path, 'w', encoding='utf-8', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(['text', 'source', 'source_url', 'date', 'id_str'])

        # Using TwitterSearchScraper to scrape data and append tweets to list
        for tweet in tqdm(sntwitter.TwitterHashtagScraper(hashtag).get_items()):
            if i > n_items:
                break
            if tweet.lang == 'en' and tweet.retweetedTweet is None:
                msg = [tweet.content, tweet.source, tweet.sourceUrl, tweet.date, str(tweet.id)]
                csvwriter.writerow(msg)
                i += 1
    return

if __name__ == '__main__':
    hashtags = ["cats", "dogs", "pets"]
    for hashtag in tqdm(hashtags):
        max_tweets = 10000
        scrape_hashtag(hashtag, hashtag + '.csv', max_tweets)
