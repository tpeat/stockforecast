from psaw import PushshiftAPI
import pandas as pd
import datetime

api = PushshiftAPI()

start_time = int(datetime.datetime(2021,3,12).timestamp())
content = list(api.search_submissions(after=start_time,subreddit='wallstreetbets', filter=['url', 'author','title','subreddit'],limit=10))

for post in content:
  print(post.created_utc)
  print(post.title)
  print(post.url)
