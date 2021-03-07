#This is the main code that was written by Mohammad H. Shahin that I had found it on Github and changed it for my own usuage
#You don't need to change anything in this code :)
import re
import requests
import json
import sys
import os

def get_download_link(link):
    media_type = re.split(r'/', link)[3]
    file_name = re.split(r'/', link)[5]
    list=[]
    feat=0
    for i in range(0,len(file_name)):
      if file_name[i]=="(":
        feat=1

    session = requests.Session()
    if media_type == "podcasts":
        response = session.get("https://www.radiojavan.com/podcasts/podcast_host/?id=%s" %(file_name))
        url = str(json.loads(response.text)['host']) + "/media/podcast/mp3-256/" + file_name + ".mp3"
#        print (url)
        os.system("wget -q " + url)

    elif media_type == "mp3s" and feat==0:
        response = session.get("https://www.radiojavan.com/mp3s/mp3_host/?id=%s" %(file_name))
        url = str(json.loads(response.text)['host']) + "/media/mp3/" + file_name + ".mp3"
#        print(url)
        os.system("wget -q " + url)

    elif media_type == "mp3s" and feat==1:
        response = session.get("https://www.radiojavan.com/mp3s/mp3_host/?id=%s" %(file_name))
        url = str(json.loads(response.text)['host']) + "/media/mp3/" + file_name + ".mp3"
        for i in range(0,len(url)):
            if url[i]=="(":
               list.append("\\")
               list.append(url[i])
            elif url[i]==")":
               list.append("\\")
               list.append(url[i])
            else:
               list.append(url[i])

        url=""
        for i in range(0,len(list)):
               url+=list[i]

        os.system("wget -q " + url)
    elif media_type == "videos" and feat==0:
        response = session.get("https://www.radiojavan.com/videos/video_host/?id=%s" %(file_name))
        url = str(json.loads(response.text)['host']) + "/media/music_video/hq/" + file_name + ".mp4"
        os.system("wget -q " + url)


    elif media_type == "videos" and feat==1:
        response = session.get("https://www.radiojavan.com/videos/video_host/?id=%s" %(file_name))
        url = str(json.loads(response.text)['host']) + "/media/music_video/hq/" + file_name + ".mp4"
        for i in range(0,len(url)):
            if url[i]=="(":
               list.append("\\")
               list.append(url[i])
            elif url[i]==")":
               list.append("\\")
               list.append(url[i])
            else:
               list.append(url[i])

        url=""
        for i in range(0,len(list)):
               url+=list[i]

        os.system("wget -q " + url)

link = sys.argv[1]
get_download_link(link)
