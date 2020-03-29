import requests
import json
import re
from subprocess import call

def get_download_link(link):
    media_type = re.split(r'/', link)[3]
    file_name = re.split(r'/', link)[5]

    session = requests.Session()
    if media_type == "podcasts":
        response = session.get("https://www.radiojavan.com/podcasts/podcast_host/?id=%s" %(file_name))
        url = str(json.loads(response.text)['host']) + "/media/podcast/mp3-256/" + file_name + ".mp3"
    elif media_type == "mp3s":
        response = session.get("https://www.radiojavan.com/mp3s/mp3_host/?id=%s" %(file_name))
        url = str(json.loads(response.text)['host']) + "/media/mp3/" + file_name + ".mp3"
    elif media_type == "videos":
        response = session.get("https://www.radiojavan.com/videos/video_host/?id=%s" %(file_name))
        url = str(json.loads(response.text)['host']) + "/media/music_video/hq/" + file_name + ".mp4"
    else:
        return None

    return url

if __name__ == "__main__":
    link = input("Enter link: ")
    download_link = get_download_link(link)
    if download_link:
        call(["wget", download_link])
    else:
        print('Sorry, unsupported link!')
