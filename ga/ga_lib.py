#!/usr/local/env python3

import csv
import numpy as np
import pandas as pd

# TODO: Down file straight from Google Drive instead?
def get_filename():
    csvfile = input('Enter filename to load: ')
    return csvfile

def load_csv():
    csvfile = get_filename()
    with open(csvfile) as infile:
        file_content = list(csv.reader(infile))
    return cleanse_content(file_content)

def cleanse_content(file_content):
    i = 0
    for row in file_content:
        try:
            if file_content[i].index('Results Breakdown') == 0:
                headers = i + 1
                clean_data = list(file_content[headers:])
                break
        except:
            # Not found throws exception
            i += 1
            continue
        i += 1
    return clean_data

def build_df():
    data = load_csv()
    df = pd.DataFrame(data[1:], columns=data[0])
    return df

def build_indexed_df(columns=['ga:date', 'ga:dimension6']):
    df = build_df()
    indexed_df = df.reset_index(drop=True).set_index(columns)
    return indexed_df
