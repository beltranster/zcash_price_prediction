import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.preprocessing import StandardScaler
import seaborn as sns
from io import BytesIO
import requests
import pathlib
import os



#This code downloads zec price data over the past 24 hrs (maximum allowed by the free API) and stores into a csv file with the date of the job
API_KEY = 'CG-AiV7v8dYPPDTVPDFn9SdM4Tj'

def get_zec_coingecko():
    url = "https://api.coingecko.com/api/v3/coins/zcash/market_chart"
    params = {
        "vs_currency": "usd",
        "days": "1"
       # "interval": "1min"
    }
    headers = {"x-cg-demo-api-key": API_KEY}
    r = requests.get(url, params=params, headers=headers)
    r.raise_for_status()
    data = r.json()

    prices = pd.DataFrame({'timestamp':[t for t,_ in data['prices']],
                        'price':[t for _,t in data['prices']],
                        'market_caps':[t for _,t in data['market_caps']],
                        'total_volumes':[t for _,t in data['total_volumes']]})
    
    prices["timestamp"] = pd.to_datetime(prices["timestamp"], unit="ms")
    return prices

zec_prices = get_zec_coingecko()

#store
date_today = pd.Timestamp.now().strftime("%Y%m%d%H%M")
filename = f"/Users/maria/springboard/Project/data/test_zec_daily_5min_coingecko_{date_today}.csv"
zec_prices.to_csv(filename)