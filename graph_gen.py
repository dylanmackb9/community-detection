"""
Graph Generation Script

Author: Dylan Mack, dylan.mackb9@gmail.com, 

Creation: July 14, 2023, 3:35pm
"""


## Imports 
import spotipy
import json
import networkx as nx
import numpy as np
import time

from collections import defaultdict
from spotipy.oauth2 import SpotifyClientCredentials


## Auth API Info
#cid = ___  # env var
#secret = ___ # env var


# Authentication - without user
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)






## EX CASE


art_list = ["Doja Cat", "Billie Eilish", "Ed Sheeran", "Luke Combs", "The Beatles"]
max_artists = 10000
queue = ["https://open.spotify.com/artist/3TVXtAsR1Inumwj472S9r4?si=q8QnLLHDQeK_eREBjv6gVA", 
          "https://open.spotify.com/artist/4q3ewBCX7sLwd24euuV69X?si=myWynfn3RxWOzlcWCLqm5Q",
          "https://open.spotify.com/artist/6eUKZXaKkcviH0Ku9w2n3V?si=GV7AWx_TTBiHf4-jSycSPA",
          "https://open.spotify.com/artist/1Xyo4u8uXC1ZmMpatF05PJ?si=PuWSh3_KRoSncOKqigFuZg",
          "https://open.spotify.com/artist/06HL4z0CvFAxyc27GXpf02?si=VmBnXWrbReGM2eq4_r2KJg"
          ] 


# CREATING RELATIONAL DICTIONARY
# Relational dictionary is list dictionary which gives nodes and their connections
# Artists is information dictionary with ids as keys and artist information as values
reldict, artists = bfs_artists(queue, max_artists)  


## BUILDING GRAPH
G = build_graph(reldict)


## Network Measures 
a = list(reldict.items())[0][-1]
b = list(reldict.items())[2][-1]
print(artists[list(reldict.items())[0][0]]['name'])
print(artists[list(reldict.items())[2][0]]['name'])

print(G.order())
print(G.degree())
print(G.nodes())

print()
set(a).isdisjoint(b)  # returns true if they are not disjoint, false if they are not disjoint 

total_connections = 0
total_followers = 0
for art in artists:
  total_connections += G.degree(art)
  total_followers += artists[art]['followers']
  print(artists[art]['name'])
  print("Number of connections: ", G.degree(art))
  print("Number of followers: ",artists[art]['followers'])
  print()

print(total_connections / G.number_of_nodes())
print(total_followers / G.number_of_nodes())

print(nx.density(G))
print(G.number_of_edges())
print(G.number_of_nodes())
numnodes = G.number_of_nodes()
numedges = G.number_of_edges()
print(numnodes * (numnodes - 1))
print((2 * numedges) / (numnodes * (numnodes - 1)))



print(max_artists, "artists gives", nx.density(G), "graph density")  # Density



