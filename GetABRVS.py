# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 20:03:58 2018

@author: Max
"""

# Get team names and abreviations from URL
import pandas as pd
import requests
from bs4 import BeautifulSoup

def gethtmltable(urlstring, tableindex = 0):
    page = requests.get(urlstring)
    soup = BeautifulSoup(page.text, 'lxml')
    
    try:
        table = soup.find('table')
        rows = table.find_all('tr')
        output_df = pd.read_html(table.prettify(), skiprows = 0, flavor = 'bs4', header = 0)[tableindex]
        return output_df
    except AttributeError as e:
        raise ValueError("No valid table found")

allrecords = gethtmltable('https://www.baseball-reference.com/about/team_IDs.shtml')
currentteams = aa.loc[aa['Last Year']=='Present']