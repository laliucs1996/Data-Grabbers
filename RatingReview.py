import http.client
import json
import time
import pandas



df =  pandas.read_csv('TV.csv', lineterminator='\n')
df2 =  pandas.read_csv('MovieCake.csv', lineterminator='\n')

id = df.TelevisionID
id2 = df2.MovieID

tvid = []
count = []
movieid = []
count2 = []
total = []
total2 = []
checkThese = [383498,
454615,
351286,
366672,
260513,
348350,
425148,
299536,
411135]
#count movie id total

# for item in id:
#     tvid.append(item)
#     count.append(0)
#     total.append(0)



for item in checkThese:
    movieid.append(item)
    count2.append(0)
    total2.append(0)


df = pandas.DataFrame(data={"totalCount": total2, "totalVotes": count2, "movieID": movieid})
df.to_csv("./MovieRatingDerp.csv", sep=',', index=False)
#
# df = pandas.DataFrame(data={"totalCount": total, "totalVotes": count, "movieID": tvid})
# df.to_csv("./TVRating.csv", sep=',', index=False)