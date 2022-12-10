# NTSB Aviation Database

This is a collection of NTSB aviation accident data in CSV format.
[The original data was in a Microsoft Database file and can be found here](https://app.ntsb.gov/avdata/Access/).

This repo also contains some Jupyter notebooks to analyze some of the data.

## Setup

The NTSB decided to use MDB for some reason.

* Mac: `brew install mdbtools`
* Linux: `sudo apt-get install mdbtools`

### Getting a list of tables

`mdb-tables ~/Downloads/avall.mdb`

### Converting mdb to csv

`mdb-export ~/Desktop/avall.mdb <TABLE> > <TABLE>.csv`
