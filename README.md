## iheartradio rhythmbox

### Prerequisites
- Python 2.7
- Beautiful Soup 4
- Rhythmbox *optional*

### Install

```bash
sudo apt install python2.7 python-pip
pip install beautifulsoup4
```

### Run

```bash
python iheartradio.py
```

A radio.json file will be generated with every stream available for each station in Canada

### Run Rhythmbox mode

```bash
python iheartradio.py --rhythmbox
```

Add --rhythmbox flag to write to default rhythmbox cache at ~/.local/share/rhythmbox/rhythmdb.xml

Note: **Make sure you have exited rhythmbox** before running the script. Otherwise rhythmbox will overwrite the cache. Reopen it once the script is complete.

Script will update existing stations and/or add new stations if you run it again in the future.

### Author

Grant Hutchinson(hutchgrant)

### License

Released under the [MIT License](LICENSE)