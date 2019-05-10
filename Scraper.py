import http.client
import json
import time
import pandas

conn = http.client.HTTPSConnection("api.themoviedb.org")

id = []
bdp = []
budget = []
genres = []
lang = []
otitle = []
overview = []
poster = []
procomp = []
releasedate = []
revenue = []
runtime = []
status = []
tagline = []
title = []
collections = []
idforg = []
genresid = []


checkThese = [383498,
454615,
351286,
366672,
260513,
348350,
425148,
299536,
411135]


payload = "{}"
second = 0

# # df = pandas.read_csv('Movie.csv', lineterminator='\n')
# idmode = df.MovieID

for i in checkThese:

    conn.request("GET", "/3/movie/" + str(i) + "?language=en-US&api_key=3eea53d21824c1deb2b6df75a006be67", payload)

    res = conn.getresponse()
    data = res.read()
    responseObject = json.loads(data)
    print(responseObject)
    # print(responseObject['release_date'])
    if 'adult' in responseObject:
        if responseObject['adult'] == False:
             if 'release_date' in responseObject:
                    ListDate = responseObject['release_date'].split('-')
                    print(ListDate)
                    if ListDate[0] != '':
                        if int(ListDate[0]) > 2000:
                            if 'original_language' in responseObject:
                                if responseObject['original_language'] == 'en':
                                    id.append(responseObject['id'])
                                    if 'budget' in responseObject:
                                        budget.append(responseObject['budget'])
                                    else:
                                        budget.append('0')
                                    if 'genres' in responseObject:
                                            genres.append(responseObject['genres'])
                                    if 'backdrop_path' in responseObject:
                                        bdp.append(responseObject['backdrop_path'])
                                    else:
                                        bdp.append('null')
                                    if 'belongs_to_collection' in responseObject:
                                        collections.append(responseObject['belongs_to_collection'])
                                    else:
                                        collections.append('null')
                                    if 'original_language' in responseObject:
                                        lang.append(responseObject['original_language'])
                                    else:
                                        lang.append('null')
                                    if 'original_title' in responseObject:
                                        otitle.append(responseObject['original_title'])
                                    else:
                                        otitle.append('null')
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
                                    else:
                                        procomp.append('null')
                                    if 'release_date' in responseObject:
                                        releasedate.append(responseObject['release_date'])
                                    else:
                                        releasedate.append('null')
                                    if 'revenue' in responseObject:
                                        revenue.append(responseObject['revenue'])
                                    else:
                                        revenue.append('null')
                                    if 'runtime' in responseObject:
                                        runtime.append(responseObject['runtime'])
                                    else:
                                        runtime.append('null')
                                    if 'status' in responseObject:
                                        status.append(responseObject['status'])
                                    else:
                                        status.append('status')
                                    if 'tagline' in responseObject:
                                        tagline.append(responseObject['tagline'])
                                    else:
                                        tagline.append('tagline')
                                    if 'title' in responseObject:
                                        title.append(responseObject['title'])
                                    else:
                                        title.append('title')
                                    print('pass')
    second += 1
    if second == 40:
        time.sleep(10.05)
        second = 0

df = pandas.DataFrame(data={"MovieID": id, "genres": genres, "budger": budget, "Language": lang, "OriginalTitle": otitle, "Overview": overview,
                            "Poster": poster, "ProductionCompanies": procomp,
                            "ReleaseDate": releasedate, "Revenue": revenue, "Runtime": runtime, "Status": status, "TagLine": tagline, "Title": title, "BelongsToCollection": collections})
df.to_csv("./MovieDerp.csv", sep=',', index=False)

