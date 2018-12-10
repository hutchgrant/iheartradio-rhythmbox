import json
import os

import requests
from bs4 import BeautifulSoup

user = os.environ.get('USER')
file = '/home/'+user+'/.local/share/rhythmbox/rhythmdb.xml'

def decide_stream_url(stream):
    if stream['streams'].get('secure_mp3_pls_stream') is not None:
        return stream['streams']['secure_mp3_pls_stream']
    elif stream['streams'].get('secure_shoutcast_stream') is not None:
        return stream['streams']['secure_shoutcast_stream']
    elif stream['streams'].get('secure_hls_stream') is not None:
        return stream['streams']['secure_hls_stream']
    else: 
        return stream['streams']['pls_stream']

def iterate_xml(radio):
    exists = False
    for entry in soup.findAll('entry', {"type": 'iradio'}):
        if entry.title.text == radio['name']:
            exists = True
            entry.location.string = decide_stream_url(radio)
    if not exists:
        entry = soup.new_tag('entry', type="iradio")
        title = soup.new_tag('title')
        title.string = radio['name']
        entry.append(title)

        genre = soup.new_tag('genre')
        genre.string = radio['genre']
        entry.append(genre)

        artist = soup.new_tag('artist')
        entry.append(artist)

        album = soup.new_tag('album')
        entry.append(album)

        location = soup.new_tag('location')
        location.string = decide_stream_url(radio)
        entry.append(location)


        playcount = soup.new_tag('play-count')
        playcount.string = '0'
        entry.append(playcount)

        lastplayed = soup.new_tag('last-played')
        lastplayed.string = '1544363757'
        entry.append(lastplayed)

        bitrate = soup.new_tag('bitrate')
        bitrate.string = '48'
        entry.append(bitrate)

        date = soup.new_tag('date')
        date.string = '0'
        entry.append(date)

        mediatype = soup.new_tag('media-type')
        mediatype.string = "application/octet-stream"
        entry.append(mediatype)

        soup.rhythmdb.append(entry)
def openDB():
    global soup
    xmlHandler = open(file).read()
    soup = BeautifulSoup(xmlHandler, "xml")
def writeDB():
    f = open(file, "w")
    f.write(str(soup))
    f.close()
