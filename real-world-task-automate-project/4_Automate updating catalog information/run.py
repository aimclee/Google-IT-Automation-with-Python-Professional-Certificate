#! /usr/bin/env python3
import os
import requests
import json

# txt 파일이 있는 경로 (001.txt...010.txt)
# /supplier-data/descriptions
'''
Avocado
200 lbs
Avocado contains large amount of oleic acid, a type of monounsaturated fat that can replace saturated fat in the diet, which is very effective in reducing cholesterol levels. Avocado is al$
'''

for txt_file in os.listdir('./supplier-data/descriptions/'):
  json_dict={}
  with open(txt_file) as txt_file:
    txt_file.readlines()
    json_dict['name'] = txt_file[0].strip('\n')
    json_dict['weight'] = int(txt_file[1].strip('\n').split('lbs'))
    json_dict['description'] = txt_file[2]
    json_dict['image_name'] = txt_file.strip('.txt')+'.jpeg'
  response = requests.port(url, json=json_dict)

