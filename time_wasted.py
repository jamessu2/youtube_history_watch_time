import json
import re
import urllib.request

# from pytube import YouTube


print("***** Calculating time wasted on Youtube *****")

api_key = "AIzaSyCiDDX-Nm8dLqQ0Id59YNhzJDss6RkGjZg"
video_id = "pSudEWBAYRE"	# EXO's Love Shot MV


url_snippet = f"https://www.googleapis.com/youtube/v3/videos?part=snippet&id={video_id}&key={api_key}"

json_url_snippet = urllib.request.urlopen(url_snippet)
data_snippet = json.loads(json_url_snippet.read())

print(data_snippet['items'][0]['snippet']['title'])



url_content_details = f"https://www.googleapis.com/youtube/v3/videos?part=contentDetails&id={video_id}&key={api_key}"

json_url_content_details = urllib.request.urlopen(url_contentDetails)
data_content_details = json.loads(json_url_content_details.read())

print(data_content_details['items'][0]['contentDetails']['duration'])













