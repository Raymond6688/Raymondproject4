import praw
import random
import time
import datetime


reddit = praw.Reddit('bot')

submissions = list(reddit.subreddit("cs40_2022fall").hot(limit=5))

subreddit = list(reddit.subreddit('soccer').top(limit=500))

for i in range(300):
    newsubmission = random.choice(subreddit)

    selftext = newsubmission.selftext
    title = newsubmission.title

    if selftext == "":
        url = newsubmission.url
        reddit.subreddit('cs40_2022fall').submit(title, url=url)
        print('linkpost')
    else:
        reddit.subreddit('cs40_2022fall').submit(title, selftext = selftext)
        print('textpost')

    time.sleep(7)
