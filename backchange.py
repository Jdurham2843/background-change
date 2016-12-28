from imgurpython import ImgurClient
from credentials import creds
from random import randint
import urllib
import os

client_id = creds['client_id']
client_secret = creds['client_secret']

client = ImgurClient(client_id, client_secret)

items = client.subreddit_gallery('earthporn', sort='time', window='week', page=0)

rand = randint(0, len(items) - 1)
image_id = items[rand].id

url = client.get_image(image_id).link

local_name = 'image.' + url[-3:]

urllib.request.urlretrieve(url, local_name)

os.system('gsettings set org.cinnamon.desktop.background picture-uri "file:///home/john/PythonStuff/backchange/' + local_name + '"')


