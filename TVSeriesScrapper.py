import http.client
import json
import time
import pandas

conn = http.client.HTTPSConnection("api.themoviedb.org")

id = []
bdp = []
createdby = []
lang = []
oname = []
overview = []
poster = []
procomp = []
firstairdate = []
runtime = []
status = []
name = []
last_air_date = []
genres = []
networks = []
numberofepisodes = []
numberofseasons = []
type2 = []
seasons = []
netid = []
proid = []

seasonIDList = []

payload = "{}"
second = 0

df =  pandas.read_csv('TVTest.csv', lineterminator='\n')
d =  df.TelevisionID

for x in d:
    conn.request("GET", "/3/tv/" + str(x) + "?language=en-US&api_key=3eea53d21824c1deb2b6df75a006be67", payload)

    res = conn.getresponse()
    data = res.read()
    responseObject = json.loads(data)
    print(responseObject)
    # print(responseObject['release_date'])
    if 'origin_country' in responseObject:
        if len(responseObject['origin_country']) != 0:
            if responseObject['origin_country'][0] == 'US' or responseObject['origin_country'][0] == 'UK':
                if len(responseObject['type']) != 0:
                    if responseObject['type'] == 'Scripted' or responseObject['type'] == 'Reality' or responseObject['type'] == 'Talk Show':
                        if 'first_air_date' in responseObject:
                            if responseObject['first_air_date'] is None:
                                second += 1
                                if second == 40:
                                    time.sleep(10.05)
                                    second = 0
                                continue
                            if int(responseObject['vote_average']) > 6.9:
                                DateList = responseObject['first_air_date'].split('-')
                                if len(DateList) != 0  and int(DateList[0]) > 2005:
                                    if 'id'  in responseObject:
                                        id.append(responseObject['id'])
                                        print('pass')
                                        if 'backdrop_path' in responseObject:
                                            bdp.append(responseObject['backdrop_path'])
                                        else:
                                            bdp.append('null')
                                        if 'created_by' in responseObject:
                                            createdby.append(responseObject['created_by'])
                                        else:
                                            createdby.append('null')
                                        if 'original_language' in responseObject:
                                            lang.append(responseObject['original_language'])
                                        else:
                                            lang.append('null')
                                        if 'overview' in responseObject:
                                            overview.append(responseObject['overview'])
                                        else:
                                            overview.append('null')
                                        if 'poster_path' in responseObject:
                                            poster.append(responseObject['poster_path'])
                                        else:
                                            poster.append('null')
                                        if 'production_companies' in responseObject:
                                            procomp.append(responseObject['production_companies'])
                                            for i in responseObject['production_companies']:
                                                proid.append(i['id'])
                                        else:
                                            procomp.append('null')
                                        if 'first_air_date' in responseObject:
                                            firstairdate.append(responseObject['first_air_date'])
                                        else:
                                            firstairdate.append('null')
                                        if 'episode_run_time' in responseObject:
                                            runtime.append(responseObject['episode_run_time'])
                                        else:
                                            runtime.append('null')
                                        if 'name' in responseObject:
                                            name.append(responseObject['name'])
                                        else:
                                            name.append('null')
                                        if 'last_air_date' in responseObject:
                                            last_air_date.append(responseObject['last_air_date'])
                                        else:
                                            last_air_date.append('null')
                                        if 'genres' in responseObject:
                                            genres.append(responseObject['genres'])
                                        if 'networks' in responseObject:
                                            networks.append(responseObject['networks'])
                                            for i in responseObject['networks']:
                                                netid.append(i['id'])
                                        else:
                                            networks.append('null')
                                        if 'number_of_episodes' in responseObject:
                                            numberofepisodes.append(responseObject['number_of_episodes'])
                                        else:
                                            numberofepisodes.append('null')
                                        if 'status' in responseObject:
                                            status.append(responseObject['status'])
                                        else:
                                            status.append('null')
                                        if 'number_of_seasons' in responseObject:
                                            numberofseasons.append(responseObject['number_of_seasons'])
                                        else:
                                            numberofseasons.append('null')
                                        if 'type' in responseObject:
                                            type2.append(responseObject['type'])
                                        else:
                                            type2.append('null')
                                        if 'seasons' in responseObject:
                                            seasons.append(responseObject['seasons'])
                                            for item2 in responseObject['seasons']:
                                                seasonIDList.append(item2['id'])
                                        else:
                                            seasons.append('null')





    second += 1
    if second == 40:
        time.sleep(10.05)
        second = 0

print(len(id))
print(len(bdp))
print(len(createdby))
print(len(lang))
print(len(overview))
print(len(poster))
print(len(procomp))
print(len(firstairdate))
print(len(numberofepisodes))
print(len(numberofseasons))
print(len(runtime))
print(len(status))
print(len(networks))
print(len(name))
print(len(seasons))
print(len(last_air_date))
print(len(type2))
# df = pandas.DataFrame(data={"TelevisionID": id, "BackDropPoster": bdp, "CreatedBy": createdby, "Language": lang, "Overview": overview,
#                             "Poster": poster, "ProductionCompanies": procomp,
#                             "FirstAirDate": firstairdate, "NumberOfEpisodes": numberofepisodes, "NumberOfSeasons": numberofseasons, "EpisodeRunTime": runtime, "Status": status, "Networks": networks, "Name": name, "Seasons": seasons, "LastAirDate": last_air_date, "Type": type2, "Genre" : genres})
# df.to_csv("./TV.csv", sep=',', index=False)

df2 = pandas.DataFrame(data={"ProID": proid})
df2.to_csv("./Procomp.csv", sep=',', index=False)

df25 = pandas.DataFrame(data={"NetID": netid})
df25.to_csv("./Network.csv", sep=',', index=False)


df3 = pandas.DataFrame(data={"ID": seasonIDList})
df3.to_csv("./SeasonIDs.csv", sep=',', index=False)