"""
Services, Func on obj

Author: Dylan Mack, dylan.mackb9@gmail.com, 

Creation: July 14, 2023, 3:35pm
"""



def bfs_artists(start, max_artists):
  """
  Browsing through related artists as breadth first search
  Returning dictionary of lists with connections
  """


  show_artists = max_artists / 1000
  follower_threshold = 1000 

  queue = []  # queue, filled with artist objects
  artist_seen = set()  # seen, filled with artist objects
  artist_map = defaultdict(list)  # dictionary, keys are IDs, values are lists 


  for current_id in start:
    current_artist = sp.artist(current_id)
    current_artist_object = Artist(current_id, current_artist["name"], current_artist["followers"]["total"], current_artist["genres"])
    artist_seen.add(current_artist_object)
    queue.append(current_artist_object)

  
  while queue and len(artist_seen) < max_artists:
    start = time.time()
    current = queue.pop(0)
    related_artists = sp.artist_related_artists(current.id)
    
    for artist in related_artists["artists"]:
      if artist["followers"]["total"] < follower_threshold:
        continue # skipping to next artist in queue

      related = Artist(artist["id"], artist["name"], artist["followers"]["total"], artist["genres"])
      artist_map[current.id].append(related.id)

      if related not in artist_seen:  # if we have not seen 
        queue.append(related)
        if len(artist_seen) % show_artists == 0:
          end = time.time()
          print("The time of execution of above program is :", (end-start), "s")
          print("Current number of artists seen: ", len(artist_seen))
          print()
          start = time.time()

      artist_seen.add(related)


  my_artists = {}
  for artist in artist_seen:
    my_artists[artist.id] = vars(artist)  # vars returns a dict of object atrs and values

  return artist_map, my_artists



def build_graph(related_artist_dict):
	"""
  Build a graph from a list of related artists
  """

	G = nx.Graph()
	for artist, related in related_artist_dict.items():
		for next_artist in related:
			G.add_edge(artist, next_artist)
	return G





def degreeDict(G):
  """
  Builds a dictionary where keys are artists and values are their degree
  """

  t = 0
  for i in G.degree():
    t += 1
    print(artists[i[0]]['name'] , i[-1])
    if t == 6000:
      break
