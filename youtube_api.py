from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from oauth2client.tools import argparser
import pandas as pd

DEVELOPER_KEY = "#API_KEY"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

# build(googleapiclient.discovery) 객체 생성
youtube = build(YOUTUBE_API_SERVICE_NAME,YOUTUBE_API_VERSION,developerKey=DEVELOPER_KEY)

name_list = [search_keyword]

for n in name_list:
    videos=[]
    search_response2 = youtube.search().list(
    q = n,
    order = "relevance",
    part = "snippet",
    maxResults = 50
    ).execute()
    for search_result in search_response2.get("items", []):
        if search_result["id"]["kind"] == "youtube#video":
            videos.append("%s" % (search_result["id"]["videoId"]))
    for i in videos:
        search_response = youtube.videos().list(
        id = i,
        part = "snippet, statistics"
        ).execute()

        for search_result in search_response.get("items", []):
            List=[]
            if search_result["kind"] == "youtube#video":
                List.append(n)
                try:
                    List.append("%s" %(search_result["snippet"]["title"]))
                except KeyError:
                    List.append('')           
                try:
                    List.append("%s" %(search_result["snippet"]["tags"]))
                except KeyError:
                    List.append('')
                try:
                    List.append("%s" %(search_result["statistics"]["viewCount"]))
                except KeyError:
                    List.append('')
                try:
                    List.append("%s" %(search_result["statistics"]["likeCount"]))
                except KeyError:
                    List.append('')           
                try:
                    List.append("%s" %(search_result["statistics"]["dislikeCount"]))
                except KeyError:
                    List.append('')
                try:
                    List.append("%s" %(search_result["statistics"]["favoriteCount"]))
                except KeyError:
                    List.append('')
                try:
                    List.append("%s" %(search_result["statistics"]["commentCount"]))
                except KeyError:
                    List.append('')
            videos2.append(List)
            
            
dt = pd.DataFrame(videos2, columns =  ["name","title", "tag", "viewCount", "likeCount", "dislikeCount", "favoriteCount", "commentCount"]) 
dt.to_csv("da.csv", encoding='utf-8-sig')
