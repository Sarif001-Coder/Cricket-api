import requests

#authurl = f"https://Cricbuzz-Official-Cricket-API.proxy-production.allthingsdev.co/home"
#NEWS = "https://Cricbuzz-Official-Cricket-API.proxy-production.allthingsdev.co/series/4471/news"
url2 = "https://Cricbuzz-Official-Cricket-API.proxy-production.allthingsdev.co/matches/upcoming"

HEADERS = {
    "x-apihub-key": "UUq-DZR6PF-1z2I4p07mnCtArZ5zp9wa1TNCziv8fU01c2ucld",
    "x-apihub-host": "Cricbuzz-Official-Cricket-API.allthingsdev.co",
    "x-apihub-endpoint": "f0e25fa6-e8a8-47f7-affb-db42c580e582"
}

# def api_info_check():
#     try:
#         responseAPI = requests.get(authurl, headers=HEADERS, timeout=5)
#         if responseAPI.status_code == 200:
#             return print("API is working")
#         else:
#             print("API not working")
#     except requests.exceptions.RequestException as e:
#         return print("Wrong API details")

# Fetch Series news
# def cricket_news():
#     try:
#         news_response = requests.get(NEWS, headers=HEADERS, timeout=5)
#         # Status code verification
#         if news_response.status_code == 200:
#            return news_response.json()
#         else:
#            print("No respose from API - ", str(news_response.status_code))
#     except requests.exceptions.RequestException as e:
#         raise Exception("API request failed: {e}")
    
def Future_match():
    try:
        fmatch = requests.get(url2,headers=HEADERS, timeout=5) 
        if fmatch.status_code == 200:
            FM = fmatch.json()
            print("Types of Format: ",f"{FM['filters']}")
            print("Matches : ",FM['typeMatches'][3]["seriesMatches"][0])
        else:
            return print("nothing found")
    except requests.exceptions.RequestException as e:
        raise Exception("API request failed. {e}")

# Parse news.
# def parse_news(news_response):
#     parsed = []
#     for item in news_response.get("storyList",[]):
#         story = item.get("story")
#         if not story:
#             continue
#         hline = story.get("hline","").strip()
#         intro = story.get("intro","").strip()
#         seoHeadline = story.get("seoHeadline", "").strip()
#         context = story.get("context", "").strip()
#         #
#         if not any([hline, intro, seoHeadline, context]):
#             continue
#         #
#         parsed.append({
#             "hline": hline,
#             "intro": intro,
#             "seoHeadline": seoHeadline,
#             "context": context
#         })
#     return parsed
# 
# def upcoming_match_parse(match):
#     parsed=[]
#     for matchinfo in match.get("matches", []):
#         parsed.append({
#             "team1": matchinfo["team1"],
#             "team2": matchinfo["team2"],
#             "date": matchinfo["date"]
#         })
#     return parsed