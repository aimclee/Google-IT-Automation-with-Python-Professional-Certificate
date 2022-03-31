#! /usr/bin/env python3

import os
import requests

PATH = '/data/feedback/'
keys=['title','name','date','feedback']


for file in os.listdir(PATH):
  key_cnt=0
  feedback={}
  with open(PATH+file) as f:
    for line in f:
      value=line.strip()
      feedback[keys[key_cnt]] = value
      key_cnt+=1
  print(feedback)
  response = requests.post('http://34.71.12.113/feedback/',json=feedback)
print(response.request.body)
print(response.status_code)
