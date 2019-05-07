import http.client
import json
import time
import pandas

conn = http.client.HTTPSConnection("api.themoviedb.org")
payload = "{}"
second = 0

df =  pandas.read_csv('TV.csv', lineterminator='\n')
d =  df.TelevisionID
s = df.NumberOfSeasons

tvid = []
id = []
air_date = []
name = []
overview = []
poster_path = []
season_number = []

episodeNo = []
tvIDEp = []
airDateEpi = []
guest = []
overview2 = []
season_id = []
still_path = []
epiName = []
epiCrew = []

for d,s in df.iterrows():
    print("pass")
    for i in (1, s['NumberOfSeasons'] + 1):
        conn.request("GET", "/3/tv/" + str(s['TelevisionID']) + "/season/" + str(i) + "?language=en-US&api_key=3eea53d21824c1deb2b6df75a006be67", payload)
        res = conn.getresponse()
        data = res.read()
        responseObject = json.loads(data)
        print(responseObject)
        if 'status_code' not in responseObject:
            if 'id' in responseObject:
                id.append(responseObject['id'])
            else:
                id.append("null")
            tvid.append(s['TelevisionID'])
            if 'air_date' in responseObject:
                air_date.append(responseObject['air_date'])
            else:
                air_date.append('null')
            if 'episodes' in responseObject and responseObject['episodes'] != '[]':
                for items in responseObject['episodes']:
                    tvIDEp.append(s['TelevisionID'])
                    season_id.append(responseObject['id'])
                    if 'episode_number' in items:
                        episodeNo.append(items['episode_number'])
                    else:
                        episodeNo.append(0)
                    if 'air_date' in items:
                        airDateEpi.append(items['air_date'])
                    else:
                        airDateEpi.append('null')
                    if 'name' in items:
                        epiName.append(items['name'])
                    else:
                        epiName.append('null')
                    if 'guest_stars' in items and items['guest_stars'] != []:
                        guest.append(items['guest_stars'])
                    else:
                        guest.append('null')
                    if 'overview' in items:
                        overview2.append(items['overview'])
                    else:
                        overview2.append('null')
                    if 'crew' in items and items['crew'] != []:
                        epiCrew.append(items['crew'])
                    else:
                        epiCrew.append('null')
                    if 'still_path' in items:
                        still_path.append(items['still_path'])
                    else:
                        still_path.append('null')
            if 'name' in responseObject:
                name.append(responseObject['name'])
            else:
                name.append('null')
            if 'poster_path' in responseObject:
                poster_path.append(responseObject['poster_path'])
            else:
                poster_path.append('null')
            if 'season_number' in responseObject:
                season_number.append(responseObject['season_number'])
            else:
                season_number.append('null')
            if 'overview' in responseObject:
                overview.append(responseObject['overview'])
            else:
                overview.append('null')
        second += 1
        if second == 40:
            time.sleep(10.05)
            second = 0

df2 = pandas.DataFrame(data={"tvID": tvid, "tvSeasonID": id, "airDate": air_date,  "name": name, "overview": overview, "posterPath": poster_path, "seasonNo": season_number})
df2.to_csv("./TVSeasons.csv", sep=',', index=False)


df2 = pandas.DataFrame(data={"televisionID": tvIDEp, "airDate": airDateEpi,  "name": epiName, "overview": overview2, "posterPath": still_path, "seasonID": season_id, "guest": guest, "episodeNo": episodeNo, 'crew': epiCrew, 'name': epiName})
df2.to_csv("./TVEpisodes.csv", sep=',', index=False)



# epiName = []
# epiCrew = []