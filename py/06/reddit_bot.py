import praw
import pandas as pd
import datetime as dt


reddit = praw.Reddit(client_id='USE YOURS',
                     client_secret='USE YOURS',
                     user_agent='USE YOURS')

print(reddit.read_only)
for submission in reddit.subreddit('learnpython').hot(limit=10):
    print(submission.title)

subreddit = reddit.subreddit('TurkeyJerky')

print(subreddit.title)

for submission in subreddit.hot(limit=10):
    print(submission.title)  # Output: the submission's title
    print(submission.score)  # Output: the submission's score
    print(submission.id)     # Output: the submission's ID
    print(submission.url)    # Output: the URL the submission points to
                             # or the submission's URL if it's a self post