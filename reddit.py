from psaw import PushshiftAPI
import pandas as pd
import datetime
import numpy as np

api = PushshiftAPI()

start_time = int(datetime.datetime(2021,3,12).timestamp())
content = api.search_submissions(after=start_time,
                                 subreddit='wallstreetbets',
                                 filter=['url', 'author','title','subreddit'])

df = pd.DataFrame(content)
for post in content:
    words = post.title.split()
    cashtags = list(set(filter(lambda word: word.lower().startswith('$'), words)))
    if len(cashtags) > 0:
      print(cashtags)
      print(content.title)
 # print(post.created_utc)
 # print(post.title)
 # print(post.url)

