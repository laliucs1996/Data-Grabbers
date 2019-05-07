import http.client
import json
import time
import pandas

name = []
overview = []
poster_path = []
bdp = []
parts = []
CollID = []
second = 0
df =  pandas.read_csv('Collections.csv', lineterminator='\n')
id =  df.ID
conn = http.client.HTTPSConnection("api.themoviedb.org")

for i in id:
    conn.request("GET", "/3/collection/" + str(i) + "/credits?api_key=3eea53d21824c1deb2b6df75a006be67", payload)
    res = conn.getresponse()
    data = res.read()
    responseObject = json.loads(data)
    CollID.append(i)
    if 'name' in responseObject:
        name.append(responseObject['name'])
    else:
        name.append('0')
    if 'overview' in responseObject: zx
        overview.append(responseObject['overview'])
    else:
        overview.append('null')
    if 'poster_path' in poster_path:
        poster_path.append(responseObject['poster_path'])
    else:
        poster_path.append('null')
    if 'backdrop_path' in responseObject:
        bdp.append(responseObject['backdrop_path'])
    else:
        bdp.append('null')
    if 'parts' in responseObject:
        parts.append(responseObject['parts'])
    else:
        parts.append('null')
    second += 1
    if second == 40:
        time.sleep(10.05)
        second = 0
df = pandas.DataFrame(data={"Name": name, "CollectionID": CollID, "Overview": overview, "BackDropPoster": ndp, "PosterPath": poster_path, "Parts": parts})
df.to_csv("./Collection.csv", sep=',', index=False)