# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 14:36:05 2018

@author: reddem
"""

# importing the requests library
import requests

# api-endpoint
url1 ="https://jsonmock.hackerrank.com/api/movies/search/?Title="
substr=raw_input("Please enter search string:")
URL=url1+substr
print URL
r = requests.get(url = URL)
data = r.json()

print("total", data['total'])
