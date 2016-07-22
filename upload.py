import os
import json
import requests


def uploadFile(filename):

  page_id = '437575193035602'
  token = os.environ.get('AHA_ROBOT_COMMUNITY_GODZILLA_FB')
  payload = {"access_token":token}
  files = {"files":open(os.path.dirname(os.path.abspath(__file__))+'/img/'+filename,'rb')}
  file = requests.post('https://graph.facebook.com/v2.6/'+page_id+'/photos',params=payload,files=files)
  print(file.text)
  a = json.loads(file.text)
  with open('./img_list.csv','a+') as f:
    f.write(",".join([a['id'],filename])+"\n")
uploadFile('2.png')
uploadFile('hi.png')
uploadFile('hi2.png')
uploadFile('night.png')
uploadFile('sunset.png')
