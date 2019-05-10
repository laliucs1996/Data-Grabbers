import http.client
import json
import time
import pandas

df =  pandas.read_csv('MovieDerp.csv', lineterminator='\n')
id =  df.MovieID
conn = http.client.HTTPSConnection("api.themoviedb.org")

idList = []
posterURL = []
second = 0
payload = "{}"
for i in id:
    conn.request("GET", "/3/Movie/" + str(i) + "/images?api_key=3eea53d21824c1deb2b6df75a006be67", payload)
    # print(i)
    res = conn.getresponse()
    data = res.read()
    responseObject = json.loads(data)
    print(responseObject)
    if 'backdrops' not in responseObject:
        second += 1
        if second == 40:
            time.sleep(10.05)
            second = 0
        continue
    for items in responseObject['backdrops']:
        idList.append(i)
        posterURL.append(items['file_path'])
    second += 1
    if second == 40:
        time.sleep(10.05)
        second = 0
df = pandas.DataFrame(data={"poster": posterURL, "movieID": idList})
df.to_csv("./TVPoster.csv", sep=',', index=False)