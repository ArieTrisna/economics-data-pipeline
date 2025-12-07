# Importing Libraries
import requests
import json
import pandas as pd
import wbgapi as wb
from pathlib import Path

def get_data():
    gdp_data = wb.data.DataFrame('NY.GDP.PCAP.CD')
    inflation_data = wb.data.DataFrame('NY.GDP.DEFL.KD.ZG')
    unemployment_data = wb.data.DataFrame('SL.UEM.TOTL.NE.ZS')

    return gdp_data, inflation_data, unemployment_data

def filter_to_jpn():
    gdp_data, inflation_data, unemployment_data = get_data()
    
    jpn_gdp = gdp_data.filter(items=['JPN'], axis=0)
    jpn_inflation = inflation_data.filter(items=['JPN'], axis=0)
    jpn_unemployment = unemployment_data.filter(items=['JPN'], axis=0)
    
    return jpn_gdp, jpn_inflation, jpn_unemployment

def transform():
    jpn_gdp, jpn_inflation, jpn_unemployment = filter_to_jpn()
    
    jpn_gdp = jpn_gdp.rename(index={'JPN' : 'gdp'})
    jpn_inflation = jpn_inflation.rename(index={'JPN' : 'inflation'})
    jpn_unemployment = jpn_unemployment.rename(index={'JPN' : 'unemployment'})
    
    jpn_econ = pd.concat([jpn_gdp, jpn_inflation, jpn_unemployment], axis=0)
    jpn_econ = jpn_econ.transpose()
    jpn_econ = jpn_econ.rename_axis('year')

    return jpn_econ

def extract_to_csv():
    jpn_econ = transform()
    
    filepath = Path('data/jpn_econ.csv')
    filepath.parent.mkdir(parents=True, exist_ok=True) 
    jpn_econ.to_csv(filepath, index=True)

if __name__ == "__main__":
    extract_to_csv()