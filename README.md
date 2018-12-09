## iheartradio scraper

### Prerequisites
- Python 2.7
- Beautiful Soup 4

### Install

```bash
sudo apt install python2.7 python-pip
pip install beautifulsoup4
```

### Run

```bash
python iheartradio.py
```

A radio.json file will be generated with every stream available for each station in canada

### Run Rhythmbox mode

Add --rhythmbox flag to initiate a write to the default rhythmbox cache at ~/.local/share/rhythmbox/rhythmboxdb.xml

Note: **Make sure you have exited rhythmbox** before running the script. Otherwise rhythmbox will overwrite the cahce. Reopen it once the script is complete.

```bash
python iheartradio.py --rhythmbox
```

Script will update existing stations and/or add new stations if you run it again in the future.

### Author

Grant Hutchinson(hutchgrant)

### License

Released under the [MIT License](LICENSE)