import requests
import json
import re
from subprocess import call


def get_download_link(link):
    media_type = re.split(r"/", link)[3]
    file_name = re.split(r"/", link)[5]

    session = requests.Session()
    response = session.get(f"https://www.radiojavan.com/{media_type}/{media_type[:-1]}_host/?id={file_name}")
    base_url = str(json.loads(response.text)["host"])
    if media_type == "podcasts":
        return f"{base_url}/media/podcast/mp3-256/{file_name}.mp3"
    elif media_type == "mp3s":
        return f"{base_url}/media/mp3/{file_name}.mp3"
    elif media_type == "videos":
        return f"{base_url}/media/music_video/hq/{file_name}.mp4"
    else:
        return None


if __name__ == "__main__":
    media_link = input("Enter a link: ")
    download_link = get_download_link(media_link)
    if download_link:
        call(["wget", download_link])
    else:
        print("Sorry, unsupported link!")
