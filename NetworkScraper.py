import http.client
import json
import time
import pandas

name = []
origin_country = []
CollID = []
headquarters = []
homepage = []
second  = 0
df =  pandas.read_csv('Company.csv', lineterminator='\n')
id =  df.ID
conn = http.client.HTTPSConnection("api.themoviedb.org")

for i in id:
    conn.request("GET", "/3/network/" + str(i) + "/credits?api_key=3eea53d21824c1deb2b6df75a006be67", payload)
    res = conn.getresponse()
    data = res.read()
    responseObject = json.loads(data)
    CollID.append(i)
    if 'name' in responseObject:
        name.append(responseObject['name'])
    else:
        name.append('0')
    if 'headquarters' in responseObject:
        headquarters.append(responseObject['headquarters'])
    else:
        headquarters.append('null')
    if 'homepage' in responseObject:
        homepage.append(responseObject['homepage'])
    else:
        homepage.append('null')
    if 'origin_country' in responseObject:
        origin_country.append(responseObject['origin_country'])
    else:
        origin_country.append('null')
    second += 1
    if second == 40:
        time.sleep(10.05)
        second = 0

df = pandas.DataFrame(data={"Name": name, "Headquarters": headquarters, "ID": id, "Homepage": homepage, "OriginCountry": origin_country})
df.to_csv("./Collection.csv", sep=',', index=False)