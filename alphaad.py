#!/usr/bin/env python3

import requests
#import alpha_vantage
import json


API_URL = "https://www.alphavantage.co/query"
symbols = ['VZ',"T","S"]

for symbol in symbols:
        data = { "function": "TIME_SERIES_DAILY",
        "symbol": symbol,
        "interval" : "Daily",
        "datatype": "json",
        "apikey": "7248MEY0N5KK2G1U" }
        response = requests.get(API_URL, data)
        data = response.json()
        print(symbol)
        a = (data['Time Series (Daily)'])
        keys = (a.keys())
        for key in keys:
                print("Open " + a[key]['1. open'] + " High " + a[key]['2. high'] + " Low " + a[key]['3. low'] + " Close " + a[key]['4. close'])
