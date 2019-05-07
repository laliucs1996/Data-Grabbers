import http.client
import json
import time
import pandas

df =  pandas.read_csv('Person.csv', lineterminator='\n')
id =  df.PeopleID
conn = http.client.HTTPSConnection("api.themoviedb.org")


peopleID = []
character = []
movieID = []

peopleIDB = []
department = []
job = []
movieIDB = []

peopleIDAB = []
characterAB = []
tvID = []

peopleIDBB = []
departmentBB = []
jobBB = []
tvIDBB = []


second = 0
payload = "{}"
for i in id:
    conn.request("GET", "/3/person/" + str(i)  + "/movie_credits?language=en-US&api_key=3eea53d21824c1deb2b6df75a006be67", payload)
    # print(i)
    res = conn.getresponse()
    data = res.read()
    responseObject = json.loads(data)
    print(responseObject)
    if 'cast' in responseObject and responseObject['cast'] != '[]' and responseObject['cast'] != '':
        for item in responseObject['cast']:
            if 'id' in item:
                movieID.append(item['id'])
                peopleID.append(i)
                if 'character' in item:
                    character.append(item['character'])
                else:
                    character.append('null')

    if 'crew' in responseObject and responseObject['crew'] != '[]' and responseObject['crew'] != '':
        for item in responseObject['crew']:
            if 'id' in item:
                movieIDB.append(item['id'])
                peopleIDB.append(i)
                if 'department' in item:
                    department.append(item['department'])
                else:
                    department.append('null')
                if 'job' in item:
                    job.append(item['job'])
                else:
                    job.append('null')

    conn.request("GET","/3/person/" + str(i) + "/tv_credits?language=en-US&api_key=3eea53d21824c1deb2b6df75a006be67",payload)
    # print(i)
    res = conn.getresponse()
    data = res.read()
    responseObject = json.loads(data)
    print(responseObject)
    if 'cast' in responseObject and responseObject['cast'] != '[]' and responseObject['cast'] != '':
        for item in responseObject['cast']:
            if 'id' in item:
                tvID.append(item['id'])
                peopleIDAB.append(i)
                if 'character' in item:
                    characterAB.append(item['character'])
                else:
                    characterAB.append('null')
    if 'crew' in responseObject and responseObject['crew'] != '[]' and responseObject['crew'] != '':
        for item in responseObject['crew']:
            if 'id' in item:
                tvIDBB.append(item['id'])
                peopleIDBB.append(i)
                if 'department' in item:
                    departmentBB.append(item['department'])
                else:
                    departmentBB.append('null')
                if 'job' in item:
                    jobBB.append(item['job'])
                else:
                    jobBB.append('null')
    second += 2
    if second == 40:
        time.sleep(10.05)
        second = 0
df = pandas.DataFrame(data={"peopleID": peopleID, "character": character, "movieID": movieID})
df.to_csv("./PeopleMovieCast.csv", sep=',', index=False)
df = pandas.DataFrame(data={"peopleID": peopleIDB, "job": job, "movieID": movieIDB, "department": department})
df.to_csv("./PeopleMovieCrew.csv", sep=',', index=False)
df = pandas.DataFrame(data={"peopleID": peopleIDAB, "character": characterAB, "movieID": tvID})
df.to_csv("./PeopleTVCast.csv", sep=',', index=False)
df = pandas.DataFrame(data={"peopleID": peopleIDBB, "job": jobBB, "movieID": tvIDBB, "department": departmentBB})
df.to_csv("./PeopleTVCrew.csv", sep=',', index=False)
