from bs4 import BeautifulSoup
import requests
import json
import sys
import rhythmbox

writeXML = False

if len(sys.argv) > 1:
    writeXML = sys.argv[1] == "--rhythmbox"

def fetch_all_stations():
    # fetch all stations page
    page_link = 'https://www.iheart.com/live/country/CA/'
    page_response = requests.get(page_link, timeout=5)

    # parse all stations page
    page_content = BeautifulSoup(page_response.content, "html.parser")

    # fetch all station urls
    return page_content.findAll('a',attrs={"class":"thumbLink"})

def fetch_station(url):
    station = {}
    # fetch station page
    page_response = requests.get(url, timeout=15)

    # parse station page
    page_content = BeautifulSoup(page_response.content, "html.parser")
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
            print  'Added: '+station['name']
        if writeXML is True:
            rhythmbox.iterate_xml(station)

    return station

def iterate_stations(urls):
    stations = []
    for url in urls:
        stations.append(fetch_station('https://www.iheart.com'+url['href']))
    return stations

def write_stations(stations):
    f = open("radio.json", "w")
    f.write(json.dumps(stations, indent=2, sort_keys=True))
    if writeXML is True:
        rhythmbox.writeDB()

urls = fetch_all_stations()
if writeXML is True:
    rhythmbox.openDB()
stations = iterate_stations(urls)
write_stations(stations)
print 'Success! radio.json generated'
if writeXML is True:
    print 'Rhythmbox updated!'
