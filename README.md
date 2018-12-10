## iheartradio rhythmbox

### Prerequisites
- Python 3
- Rhythmbox *optional*

### Install

```bash
sudo apt install python3 python3-pip
pip install iheartradio
```

### Run

```bash
iheartradio
```

A radio.json file will be generated with every stream available for each station in Canada. You can select US radio stations as well, see below.

### Run Rhythmbox mode

```bash
iheartradio --rhythmbox
```

Add --rhythmbox flag to write to default rhythmbox cache at ~/.local/share/rhythmbox/rhythmdb.xml

Note: **Make sure you have exited rhythmbox** before running the script. Otherwise rhythmbox will overwrite the cache. Reopen it once the script is complete.

Script will update existing stations and/or add new stations if you run it again in the future.

### Country Code

You can select US radio stations by adding --country US

```bash
iheartradio --rhythmbox --country US
```

There are over 1000 US radio stations, this will take a while and I suggest you don't do it very often as it could cause a temp ban.

### Author

Grant Hutchinson(hutchgrant)

### License

Released under the [MIT License](LICENSE)