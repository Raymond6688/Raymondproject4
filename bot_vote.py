import praw
import random
import time
import datetime
from textblob import TextBlob

reddit = praw.Reddit('bot')
submissions = list(reddit.subreddit("cs40_2022fall").hot(limit=None))

for submission in submissions:
    print(f"Looking at {submission.title} now")
    if 'Trump' in submission.title:
        blob = TextBlob(submission.title)
        sum = 0
        for sentence in blob.sentences:
            sum +=(sentence.sentiment.polarity)
        if sum > 0.1:
            submission.upvote()
        else:
            submission.downvote()

    elif 'Trump' in submission.selftext:
        blob = TextBlob(submission.selftext)
        sum = 0
        for sentence in blob.sentences:
            sum +=(sentence.sentiment.polarity)
        if sum > 0.1:
            submission.upvote()
        else:
            submission.downvote()


    submission.comments.replace_more(limit=None)
    all_comments = submission.comments.list()
    for comment in all_comments:
        if 'Trump' in comment.body:
            blob = TextBlob(comment.body)
            sum = 0
            for sentence in blob.sentences:
                sum +=(sentence.sentiment.polarity)
                if sum > 0.1:
                    comment.upvote()
                else:
                    comment.downvote()
                   



    
    