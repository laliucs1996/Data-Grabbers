import http.client
import json
import time
import pandas
import urllib.request
import os

# df =  pandas.read_csv('TV.csv', lineterminator='\n')
df =  pandas.read_csv('MovieDerp.csv', lineterminator='\n')
filepath = 'https://image.tmdb.org/t/p/original'
for d,s in df.iterrows():
    print(s)
    if type(s[5]) != str:
        continue
    url = filepath + s[5].rstrip()
    print(url)
    if not os.path.exists('/Users/Larry/Downloads/' + 'MoviePoster/' + str(s['MovieID'])):
        os.makedirs('/Users/Larry/Downloads/' + 'MoviePoster/' + str(s['MovieID']))
    try:
        urllib.request.urlretrieve(url, '/Users/Larry/Downloads/' + 'MoviePoster/' + str(s['MovieID']) + s[5].rstrip())
    except urllib.error.HTTPError:
        continue