import http.client
import json
import time
import pandas


df =  pandas.read_csv('MovieDerp.csv', lineterminator='\n')
id =  df.MovieID
conn = http.client.HTTPSConnection("api.themoviedb.org")


id1 = []
personid = []
character = []
genderA  = []
nameA = []
prof_pathA = []
order = []

id2 = []
crewid = []
department = []
gender = []
job = []
name = []
prof_path = []
second = 0

payload = "{}"
for i in id:
    conn.request("GET", "/3/movie/" + str(i) + "/credits?api_key=3eea53d21824c1deb2b6df75a006be67", payload)
    # print(i)
    res = conn.getresponse()
    data = res.read()
    responseObject = json.loads(data)
    print(responseObject)
    if 'crew' in responseObject:
        for item in responseObject['crew']:
            id2.append(i)
            if 'id' in item:
                crewid.append(item['id'])
            else:
                crewid.append(0)
            if 'department' in item:
                department.append(item['department'])
            else:
                department.append('null')
            if 'gender' in item:
                gender.append(item['id'])
            else:
                gender.append('null')
            if 'job' in item:
                job.append(item['job'])
            else:
                job.append('null')
            if 'name' in item:
                name.append(item['name'])
            else:
                name.append('null')
            if 'profile_path' in item:
                prof_path.append(item['profile_path'])
            else:
                prof_path.append('null')
    if 'cast' in responseObject:
        for item in responseObject['cast']:
            id1.append(i)
            if 'id' in item:
                personid.append(item['id'])
            else:
                personid.append(0)
            if 'character' in item:
                if item['character'] == '':
                    character.append(item['name'])
                else:
                    character.append(item['character'])
            else:
                character.append('null')
            if 'gender' in item:
                genderA.append(item['id'])
            else:
                genderA.append('null')
            if 'name' in item:
                nameA.append(item['name'])
            else:
                nameA.append('null')
            if 'profile_path' in item:
                prof_pathA.append(item['profile_path'])
            else:
                prof_pathA.append('null')
            if 'order' in item:
                order.append(item['order'])
            else:
                order.append('null')
    second += 1
    if second == 40:
        time.sleep(10.05)
        second = 0




df = pandas.DataFrame(data={"movieID": id1, "character": character, "gender": genderA, "name": nameA, "profilePath": prof_pathA, "order": order, "peopleID": personid})
df.to_csv("./MovieCastDerp.csv", sep=',', index=False)

df = pandas.DataFrame(data={"movieID": id2, "peopleID": crewid, "gender": gender, "name": name, "profilePath": prof_path, "job": job, "department": department})
df.to_csv("./MovieCrewNotDerp.csv", sep=',', index=False)