#!/usr/bin/env python3

from PIL import Image
import glob

FILE_PATH = '/home/student-03-d47b29f43f00/images'

list_images = glob.glob(FILE_PATH + "*.tiff")

for image in list_images:
  img = Image.open(image)

  # tiff 확장자명 제거
  image = image.strip('.tiff')
  # width, height = img.size
  img.resize((128,128)).rotate(270).save(f'/home/student-03-d47b29f43f00/opt/icons/{image}.jpeg')



import glob
from PIL import Image
 
newsize = 128, 128
 
for file in glob.glob("ic_*"):
       im = Image.open(file).convert('RGB')
       im.rotate(270).resize((newsize)).save("/opt/icons/" + file, "JPEG")


import os
from PIL import Image

size = (128, 128)

# listdir() : 현재 디렉토리에 있는 모든 파일 리스트를 가져온다.
for infile in os.listdir():
    # infile에서 파일 이름은 0번째 인덱스에, 확장자명은 1번째 인덱스에 존재한다.
    outfile = os.path.splitext(infile)[0]
    try:
        with Image.open(infile).convert('RGB') as im:
            im.resize(size)
            im.rotate(270).save("/opt/icons/" + outfile, "JPEG")
    except OSError:
        pass


