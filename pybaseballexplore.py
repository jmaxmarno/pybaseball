# -*- coding: utf-8 -*-
"""
Created on Sat Mar  3 14:36:18 2018

@author: Max
"""

import pybaseball
import numpy as np
import pandas as pd
from pybaseball import schedule_and_record
from pybaseball import standings
import requests
from bs4 import BeautifulSoup
cyear=2018
pyear=2017

p_records = schedule_and_record(pyear, 'BOS')


standingsdata = standings(2016)

# unique Teams from batting stats
from pybaseball import team_batting
bsTeams = team_batting(2010, cyear)['Team'].unique()
#or
#list(set(team_batting(2010, cyear)['Team']))

# unique Teams from standings
from pybaseball import standings
sTeams = pd.concat(standings(pyear))['Tm'].unique()

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