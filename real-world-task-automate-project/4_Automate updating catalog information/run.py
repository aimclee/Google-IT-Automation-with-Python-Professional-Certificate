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

def data(url, description_dir):
  json_dict={}
  for txt_file in os.listdir(description_dir):
    json_dict.clear()
    file_name = os.path.join(description_dir, txt_file)
    with open(file_name) as file_name:
      line = file_name.readlines()
      json_dict['name'] = line[0].strip('\n')
      json_dict['weight'] = int(line[1].strip('\n').split('lbs'))
      json_dict['description'] = line[2].strip('\n').replace(u'\xa0',u'')
      json_dict['image_name'] = line.split('.txt')+'.jpeg'
    response = requests.post(url, json=json_dict)
  return 0


if __name__ == "__main__":
  url = 'http://localhost/fruits/'
  user = os.getenv('USER')
  description_dir = '/home/{}/supplier-data/descriptions/'.format(user)
  data(url, description_dir)