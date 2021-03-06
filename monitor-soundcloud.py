#
# monitor-soundlcoud.py
#
# by - sam nnodim
#
# adapted from: https://github.com/mikedewar/RealTimeStorytelling

# import some v useful libs
from sys import stdout
import requests
import json
import time
import random as r

# this script polls the soundcloud API, looking for new songs uploaded to
# the platform.

listofSongs = {}
url = "https://api.soundcloud.com/tracks?client_id="
apikey = "badafaf11df194b276162501eaea8bd1"

while True:
	# send a GET request to the soundcloud API and turn it to JSON data
		data = requests.get( url + apikey ).json()

		# for each song in the batch of data, get the title & artist
		for obj in data:
				# if the title isn't in the list, run the loop
				if obj["title"] not in listofSongs:
						# add the song title to list of songs
						listofSongs[obj["title"]] = obj["title"]

						# get the title, artist, genre, and link
						title = json.dumps( obj["title"] )
						artist = json.dumps( obj["user"]["username"] )
						genre = json.dumps( obj["genre"] )
						link = json.dumps( obj["permalink_url"] )

						# print the song obj. to stdout
						print '{"title":%s,"artist":%s,"genre":%s,"link":%s}'%(title, artist, genre, link)
						stdout.flush()

						# wait a little to create the image of a flowing stream
						time.sleep( r.random() )
						continue
		
		# sleep for 8 secs and poll again
		time.sleep( 8 )
