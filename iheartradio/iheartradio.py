#!/usr/bin/env python
import json
import sys

import pyfiglet
import requests
from bs4 import BeautifulSoup

from .rhythmbox import openDB, writeDB, iterate_xml 

def fetch_all_stations():
    # fetch all stations page
    page_link = 'https://www.iheart.com/live/country/'+countryCode+'/'
    page_response = requests.get(page_link, timeout=15)

    # parse all stations page
    page_content = BeautifulSoup(page_response.content, "lxml")

    # fetch all station urls
    return page_content.findAll('a',attrs={"class":"thumbLink"})

def fetch_station(url):
    station = {}
    # fetch station page
    page_response = requests.get(url, timeout=15)

    # parse station page
    page_content = BeautifulSoup(page_response.content, "lxml")
    script = page_content.find(id="initialState")
    if script is not None:
        x = json.loads(script.text)

        # parse station data
        for key in x['live']['stations']:
            station['name'] = x['live']['stations'][key]['name']
            station['description'] = x['live']['stations'][key]['description']
            station['logo'] = x['live']['stations'][key]['logo']
            station['city'] = x['live']['stations'][key]['markets'][0]['city']
            station['genre'] = x['live']['stations'][key]['genres'][0]['name']
            station['state'] = x['live']['stations'][key]['markets'][0]['stateAbbreviation']
            station['streams'] = x['live']['stations'][key]['streams']
            if x['live']['stations'][key].get('website') is not None:
                station['website'] = x['live']['stations'][key]['website']
            print  ('Added: '+station['name'])
        if writeXML is True:
            iterate_xml(station)

    return station

def iterate_stations(urls):
    stations = []
    if writeXML is True:
        openDB()
    for url in urls:
        stations.append(fetch_station('https://www.iheart.com'+url['href']))
    return stations

def write_stations(stations):
    f = open("radio.json", "w")
    f.write(json.dumps(stations, indent=2, sort_keys=True))
    if writeXML is True:
        writeDB()

def main(args):
    global writeXML
    global countryCode
    writeXML = False 
    countryCode = "CA"

    if len(args) > 1:
        i = 1
        for arg in args:
            if arg == "--rhythmbox":
                writeXML = True
            elif arg == "--country" and args[i] is not None:
                countryCode = args[i]
            i+=1
    result = pyfiglet.figlet_format("iheartradio", font = "rounded" )
    print (result) 
    print('Fetching radio stations... This could take several minutes depending on your connection and selected country code')
    urls = fetch_all_stations()
    stations = iterate_stations(urls)
    write_stations(stations)
    print ('Success! radio.json generated')
    if writeXML is True:
        print ('Rhythmbox updated!')
