import http.client
import json
import time
import pandas
from functools import reduce

conn = http.client.HTTPSConnection("api.themoviedb.org")

payload = "{}"
second = 0

aka = []
bio = []
birth = []
death = []
gender = []
id = []
hp = []
name = []
pob = []
prof_path = []

files = ['TVCastNotDerp.csv', 'TVCrewNotDerp.csv', 'MovieCastDerp.csv', 'MovieCrewNotDerp.csv',] # the 13 files
dataframes = [pandas.read_csv( f ) for f in files ] # add arguments as necessary to the read_csv method
merged = reduce(lambda left,right: pandas.merge(left,right,on='PeopleID', how='outer'), dataframes)
merged = merged.drop_duplicates(subset='PeopleID', keep = False)
merged = merged.PeopleID
print(merged)


for i in merged:
    conn.request("GET", "/3/person/" + str(i) + "?language=en-US&api_key=3eea53d21824c1deb2b6df75a006be67", payload)

    res = conn.getresponse()
    data = res.read()
    responseObject = json.loads(data)
    print(responseObject)
    if 'adult' in responseObject:
        if responseObject['adult'] == False:
            id.append(responseObject['id'])
            if 'also_known_as' in responseObject:
                aka.append(responseObject['also_known_as'])
            else:
                aka.append('null')
            if 'biography' in responseObject:
                bio.append(responseObject['biography'])
            else:
                bio.append('null')
            if 'birthday' in responseObject:
                birth.append(responseObject['birthday'])
            else:
                birth.append('null')
            if 'deathday' in responseObject:
                death.append(responseObject['deathday'])
            else:
                death.append('null')
            if 'gender' in responseObject:
                gender.append(responseObject['gender'])
            else:
                gender.append('null')
            if 'homepage' in responseObject:
                hp.append(responseObject['homepage'])
            else:
                hp.append('null')
            if 'name' in responseObject:
                name.append(responseObject['name'])
            else:
                name.append('null')
            if 'place_of_birth' in responseObject:
                pob.append(responseObject['place_of_birth'])
            else:
                pob.append('null')
            if 'profile_path' in responseObject:
                prof_path.append(responseObject['profile_path'])
            else:
                prof_path.append('null')
    second += 1
    if second == 38:
        time.sleep(10)
        second = 0

df = pandas.DataFrame(data={"AlsoKnownAs": aka, "PeopleID": id, "Biography": bio,
                            "Birthday": birth, "DeathDay": death, "Gender": gender, "Homepage": hp,
                            "Name": name, "PlaceOfBirth": pob,
                            "ProfilePath": prof_path})
df.to_csv("./Person.csv", sep=',', index=False)