# Updates the tables

import os
import shutil
import subprocess
import zipfile
from io import StringIO

import requests
import wget


def download_url(url, save_path, chunk_size=128):
    # https://stackoverflow.com/a/9419208
    r = requests.get(url, stream=True)
    with open(save_path, 'wb') as fd:
        for chunk in r.iter_content(chunk_size=chunk_size):
            fd.write(chunk)


def main():
    # Check if the data is there
    filename = 'avall'
    directory = 'raw'
    zipfile = '{}/{}.zip'.format(directory, filename)
    extracted = '{}/{}.mdb'.format(directory, filename)
    url = 'https://data.ntsb.gov/avdata/FileDirectory/DownloadFile?fileID=C%3A%5Cavdata%5Cavall.zip'

    print("Fetching data...")
    download_url(url, zipfile)

    print("Unzipping data...")
    shutil.unpack_archive(zipfile, directory)

    print("Cleaning up...")
    os.remove(zipfile)

    # Fetch
    out = subprocess.run(['mdb-tables', extracted],
                         capture_output=True, encoding="utf-8").stdout
    tables = out.split()

    # For each table, extract into CSV
    for table in tables:
        out_file = 'data/{}.csv'.format(table)
        command = ['mdb-export', extracted, table]
        output = subprocess.run(
            command, capture_output=True, encoding="utf-8").stdout
        with open(out_file, 'w') as f:
            f.write(output)

    print("Cleaning up database...")
    os.remove(extracted)


if __name__ == "__main__":
    main()
