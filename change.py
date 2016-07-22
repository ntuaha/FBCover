import os
import json
import requests
import datetime
import sys


def changeCover(targe_filename):
  page_id = '437575193035602'
  token = os.environ.get('AHA_ROBOT_COMMUNITY_GODZILLA_FB')
  target_id = None
  with open(os.path.dirname(os.path.abspath(__file__))+"/img_list.csv","r") as f:
    records = f.readlines()
  for record in records:
    (id,file) = record.strip().split(",")
    if targe_filename == file:
      target_id = id
      break
  if target_id != None:
    payload={"cover":target_id,"access_token":token}  
    file = requests.post('https://graph.facebook.com/v2.6/'+page_id,params=payload)
    print(file)
    with open('./change.log','a+') as f:
      f.write(",".join([datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),file.text])+"\n")

print(sys.argv)
if __name__ == "__main__":
  if len(sys.argv)==2:
    changeCover(sys.argv[1])  
  else:
    print("Error: Correct Command=> python3 change.py 2.png")
   