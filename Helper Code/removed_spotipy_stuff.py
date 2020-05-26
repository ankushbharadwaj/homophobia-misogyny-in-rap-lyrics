import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

SPOTIPY_CLIENT_ID =  '9afe9eae4a4647e59417875aefa1a277'
SPOTIPY_CLIENT_SECRET =  '41d06dcfb17e4b88bd47132008f3b1e7'

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id = SPOTIPY_CLIENT_ID,
                                                                             client_secret = SPOTIPY_CLIENT_SECRET))

def album_tracks(uri):
    songs = []
    for i in range(0,len(spotify.album_tracks(uri)['items'])):
        songs.append(spotify.album_tracks(uri)['items'][i]['name'])
    return(songs)

uri_list = ['spotify:album:03Mx6yaV7k4bsEmcTH8J49',
           'spotify:album:6t7956yu5zYf5A829XRiHC',
           'spotify:album:1BZoqf8Zje5nGdwZhOjAtD',
           'spotify:album:2cWBwpqMsDJC1ZUwz813lo',
           'spotify:album:11oR0ZuqB3ucZwb5TGbZxb',
           'spotify:album:0Y7qkJVZ06tS2GUCDptzyW',
           'spotify:album:1UsmQ3bpJTyK6ygoOOjG1r',
           'spotify:album:1kmyirVya5fRxdjsPFDM05',
           'Absent', #3 feet high and rising
           'spotify:album:4r1WecJyt5FOhglysp9zhN',
           'spotify:album:6vdFSyhPjL4dZFkgRtToXH',
           'Absent', #entroducing...,
           'spotify:album:18XFe4CPBgVezXkxZP6rTb',
           'spotify:album:4Uv86qWpGTxf7fU7lG5X6F',
           'spotify:album:69CmkikTHkGKdkrUZTtyWl',
           'Absent', #get rich or die tryin'
           'spotify:album:2tm3Ht61kqqRZtIYsBjxEj',
           'spotify:album:47BiFcV59TQi2s9SkBo2pb',
           'spotify:album:1zUY4PAFrNUOCeaEBrEHzh',
           'spotify:album:4eLPsYPBmXABThSJ821sqY',
           'spotify:album:0aFNb4RDk2hmKKLa0bzXNz',
           'spotify:album:3tQd5mwBtVyxCoEo4htGAV',
           'spotify:album:7AFsTiojVaB2I58oZ1tMRg',
           'spotify:album:3miZDfDnP7SmOXAJXWdFmz',
           'spotify:album:3kEtdS2pH6hKcMU9Wioob1',
           'spotify:album:5ll74bqtkcXlKE7wwkMq4g',
           'spotify:album:40GMAhriYJRO1rsY4YdrZb',
           'spotify:album:290eTJ15EAYJa3JomDWyhh',
           'spotify:album:57elsC8jWIydd3qGLf5w8C',
           'spotify:album:7ycBtnsMtyVbbwTfJwRjSP',
           'spotify:album:0vE6mttRTBXRe9rKghyr1l',
           'spotify:album:1LHacvoBTd7o2d7wwQ9EZD',
           'spotify:album:2HTbQ0RHwukKVXAlTmCZP2',
           'spotify:album:1p12OAWwudgMqfMzjMvl2a',
           'spotify:album:2pidzXTaHV4WaIJYRxKDCH',
           'spotify:album:4HUUHHXBXImwksfbSPqE7q',
           'spotify:album:1Mdy7hhoQRYdVrHzYnlUee',
           'spotify:album:20r762YmB5HeofjMCiPMLv',
           'spotify:album:5fPglEDz9YEwRgbLRvhCZy',
           'spotify:album:7dRdaGSxgcBdJnrOviQRuB',
           'spotify:album:7tsXPtLqhab1zWeubbf6JH',
           'spotify:album:2szeSQtOcJgRhDXmTS3SIf',
           'spotify:album:5BGzOpea6At0Nd7tYtYZOP',
           'spotify:track:1MWlCmgxuLIe4izcR62xBE',
           'spotify:album:5v7Icroz1sQsK2sQyLrWzE',
           'spotify:album:1ATL5GLyefJaxhQzSPVrLX',
           'spotify:album:0E47vczx9XVds1Lr2Y8rze',
           'spotify:album:6X1x82kppWZmDzlXXK3y3q',
           'spotify:album:4QrhfVaznhrAPlM5xCKBPh',
           'spotify:album:4FWvo9oS4gRgHtAwDwUjiO',
           'spotify:album:7q2B4M5EiBkqrlsNW8lB7N',
           'spotify:album:3OrucS4sHv6Bl9GS4rafEk',
           'spotify:album:3vOgbDjgsZBAPwV2M3bNOj',
           'spotify:album:5ceB3rxgXqIRpsOvVzTG28',
           'spotify:album:3kV0i1qqudjf0PGawJ4jck', #check name
           'spotify:album:7h2OEj0ifXb3UdgvTmCqfY',
           'spotify:album:2esWeP8Ln1sXA0jbDmi3Zq',
           'spotify:album:05n0d2kfwGPhKpTonLHRpY',
           'spotify:album:3AJ15ysr4Hz5p0N2tnNb1F',
           'spotify:album:4PrPbmm0gKvaD3rerOXFg8',
           'spotify:album:6eGYLONkDMja0MNtZWnRRB',
           'spotify:album:7CSP7J60QKIBCqOV64qILq',
           'spotify:album:0ptlfJfwGTy0Yvrk14JK1I',
           'spotify:album:4OGaOZUHLhSeiicZB909aL',
           'spotify:album:4tQSV1ZGpwlo3dBiTRuKvM',
           'spotify:album:2CUT0104gySOIvqwtXeFsX',
           'spotify:album:2UuvBxV56QWWj2uviGS0up',
           'spotify:album:3YPK0bNOuayhmSrs0sIIBR',
           'spotify:album:01FCoGEQ3NFWF4fHJzdiax',
           'spotify:album:7dgrVFl513aFBvMqu3KHsQ',
           'spotify:album:6trNtQUgC8cgbWcqoMYkOR',
           'spotify:album:5jem47f4IRH6UaxNAWO6vD',
           'spotify:album:5E2vrvNXeEnbFI7Ym9c9nv',
           'spotify:album:0OcMap99vLEeGkBCfCwRwS',
           'spotify:album:4v5x3Oo3UjQ9YmF3hRAip5',
           'spotify:album:4sevefzBUFvJYAzijVBQ2a',
           'spotify:album:02lktkm4J7K7N8T63Gm7KX',
           'spotify:album:78XjkzI0J1YpzKUPgzWbat',
           'spotify:album:6UkdyvPElK6JDkyeRClbI2',
           'spotify:album:3AI5kAUjgNtZBwFRi6opDc',
           'spotify:album:2xIhksIizs6gWdRBYdiTLc',
           'spotify:album:3r25XjxAmLMOhOWoV6X8N9',
           'spotify:album:2X7s6Gt8Xz2qEwlw4GVcQo',
           'spotify:album:0OknOYGLQkW3Y29gpqmYrD',
           'spotify:album:61EgDesQnFVyYf2UneM9PQ',
           'spotify:album:5PfepkNWgRR2DI02Y8AawC',
           'spotify:album:3WFTGIO6E3Xh4paEOBY9OU',
           'spotify:album:6Y7MErpA4ls6AHuTrM0qQ6',
           'spotify:album:4r3TaXjF2b1qwCpxjIpW43',
           'spotify:album:5bGumbB29JBPlv4ECVURka',
           'spotify:album:78Fgb88MY0ECc4GVMejqTg',
           'spotify:album:7btiyhWzUfzxN3ijSiBpC8',
           'spotify:album:3k8xoyOXkGgZxUKgpmxz4P',
           'Absent', #de la soul is dead
           'spotify:album:62l3f8u6j9eyDhuxsZA2iH',
           'spotify:album:0cLzuJG2UDa0axMQkF7JR6',
           'spotify:album:4k5sb7GI0J55nMSyIHJsXg',
           'spotify:album:2HOl8gDiGGpt7wsIDi9jy5',
           'spotify:album:5gK2l2LgWY0BA4p9uy27z6']

albums_df['album_uri'] = uri_list
albums_df

temp = []
didntwork = []
for i in uri_list:
    try:
        if i != 'Absent':
            temp.append(spotify.album(i)['name'])
    except:
        didntwork.append({uri_list.index(i):i})
        pass

uri_list[43] = 'spotify:album:3tqMfEzuD62nMEXALuxv6r'
temp = []
didntwork = []
for i in uri_list:
    try:
        if i != 'Absent':
            temp.append(spotify.album(i)['name'])
    except:
        didntwork.append({uri_list.index(i):i})
        pass

if len(didntwork) == 0:
    print('Good to go!')
else:
    print('Whoops: \n')
    print(didntwork)

import numpy as np
print(np.setdiff1d(albums_df['album_name'],temp))
print(np.setdiff1d(temp, albums_df['album_name']))

tracklists = {}

for uri in albums_df["album_name"]:
    tracklists[album] = album_tracks(album_uri[album])

print(tracklists)