import requests
import pandas as pd
from dateutil import parser


#This code pulls news articles published in coingecko over the past 24 hrs and stores into a file timestamped with the date

API_KEY = "pub_4e7cc7704d5c4ce68e0bb3b611a24110" 
QUERY = "zcash OR ZEC"       # search keywords
LANG = "en"                  # English news only

#url = f"https://newsdata.io/api/1/news?apikey={API_KEY}&q={QUERY}&language={LANG}"
url = f"https://newsdata.io/api/1/crypto?apikey={API_KEY}&q=zcash%20OR%20ZEC&language=en"


date_today = pd.Timestamp.now().strftime("%Y%m%d%H%M")
filename = f"/Users/maria/springboard/Project/data/news/newsdata_download_{date_today}.csv"
#timeframe for article pull
d= 4
date_limit = pd.Timestamp.today()- pd.Timedelta(days=d)

all_articles = []
page = 1

while True:
    print(f"Fetching page {page}...")
    response = requests.get(url)
    data = response.json()

    if "results" not in data or not data["results"]:
        break
    i=1
    for item in data["results"]:

        print(i, 'pubdate:', item['pubDate'])
        i+=1
        raw_date = item.get("pubDate")
        parsed_date = parser.parse(raw_date) if raw_date else None
        raw_date = pd.to_datetime(raw_date)
        

        all_articles.append({
            "pubDate": item.get("pubDate"),
            "title": item.get("title"),
            "description": item.get("description"),
            "content": item.get("content"),
            "link": item.get("link"),
            "image_url": item.get("image_url"),
            "video_url": item.get("video_url"),
            "source_id": item.get("source_id"),
            "source_url": item.get("source_url"),
            "source_priority": item.get("source_priority"),
            "creator": item.get("creator"),
            "keywords": item.get("keywords"),
            "category": item.get("category"),
            "country": item.get("country"),
            "language": item.get("language"),
            "ai_tag": item.get("ai_tag"),
            "sentiment": item.get("sentiment"),
            "duplicate": item.get("duplicate"),
            "coin": item.get("coin"),
            "article_id": item.get("article_id"),
            "fetched_at": item.get("fetched_at")
        })
        
    #stop when it gets two days of news
    if raw_date < date_limit:
        print ('Reached time limit at: ', raw_date)
        break
    # Stop if no next page
    if "nextPage" not in data or data["nextPage"] is None:
        break

    # Update URL for next page
    next_page = data["nextPage"]
    url = f"https://newsdata.io/api/1/crypto?apikey={API_KEY}&q={QUERY}&language={LANG}&page={next_page}"
    page += 1


# Save to CSV
df = pd.DataFrame(all_articles)
df.to_csv(filename, index=False)

print(f"Saved {len(df)} articles to {filename}")
