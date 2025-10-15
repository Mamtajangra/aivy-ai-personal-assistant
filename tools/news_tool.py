import requests
import os
from dotenv import load_dotenv


load_dotenv()



def get_latest_news(topic = "technology"):
    api_key_n = os.getenv("NEWS_API_KEY")
    url = f"https://newsapi.org/v2/top-headlines?q={topic}&language=en&apiKey={api_key_n}"
    response = requests.get(url).json()
    articles = response.get("articles",[])[:5]       ## if there is no article return empty list and get first 5 top news
    
    
    headlines = []  

    for a in articles:  # loop on each article
      title = a['title']  # take the title of article
      bullet_title = "• " + title  # add Bullet point 
      headlines.append(bullet_title)  # append into list
 ##
    return "Here are the top headlines:\n" + "\n".join(headlines)   ## combine all headlines
