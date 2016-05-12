'''
I looked ahead at the project code. I've decided to find more features through
the wonders of the world wide web.
'''

#import statements
import urllib
import json
import os
from time import sleep

#load list of name
DATA_DIR = os.path.join('data', 'boxofficemojo')
target_file_name = 'mojo_bladerunner.json'
target_file_path = os.path.join(DATA_DIR, target_file_name)

movie_list = []
for filename in os.listdir(DATA_DIR):
    target_file_name = filename
    target_file_path = os.path.join(DATA_DIR, target_file_name)
    with open(target_file_path, 'r') as target_file:
        movie = json.load(target_file)
    movie_list.append(movie)

names = [movie["title"] for movie in movie_list]
DATA_DIR = os.path.join('data', 'our_movies')
for title in names:
    title = title.replace(" ","+")
    url = "http://www.omdbapi.com/?t={0}+&y=&plot=short&r=json&tomatoes=true".format(title)
    jsony= json.load(urllib.urlopen(url))
    with open('OMDB_{0}.json'.format(title), 'w') as outfile:
        json.dump(jsony, outfile)
    sleep(.25)
    print jsony['title']
