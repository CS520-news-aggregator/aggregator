import requests
import json
from dotenv import load_dotenv
import os



global_exception = None
load_dotenv()
apiKey = os.getenv('API_KEY')
if apiKey:
    print("API key retrieval successful")
else:
    print("API key not found. Please check your .env file.")

class AggObject:
    def __init__(self,  title, link, media, author, date):
        self.title = title
        self.link = link
        self.media = media
        self.author = author
        self.date = date
        



def makeCallEverything(apiKey,keywords, searchIn="title", fromDate="", to="", language="en", sortBy="popularity", pageSize=5):
    url = f'https://newsapi.org/v2/everything?q={keywords}&apiKey={apiKey}&searchIn={searchIn}&from={fromDate}&to={to}&sortBy{sortBy}&language={language}&pageSize={pageSize}'
    try:
        response = requests.get(url)
        response.raise_for_status()
        response = cleanUp(response.json())
        return parseResponse(response)
    except requests.exceptions.RequestException as e:
        print(f"Failed to retrieve data: {e}")
        return None
def makeCallTopHeadline(apiKey, category, keyWords, pageSize=5, country = "us"):
    url = f'https://newsapi.org/v2/top-headlines?q={keyWords}&apiKey={apiKey}&category={category}&keyWords={keyWords}&pageSize={pageSize}&country={country}'
    try:
        response = requests.get(url)
        response.raise_for_status()
        response = cleanUp(response.json())
        return parseResponse(response)
    except requests.exceptions.RequestException as e:
        print(f'Failed to retrieve data: {e}')
        return None

def cleanUp(response):
    filtered_articles = []
    if 'articles' in response:
        for article in response['articles']:
            if article.get('title') != "[Removed]":
                filtered_articles.append(article)
    response['articles'] = filtered_articles
    return response


def parseResponse(response):
    articles=[]
    for article in response['articles']:
        temp = AggObject(article.get('title'), article.get('url'), article.get('urlToImage'), article.get('author'), article.get('publishedAt'))
        articles.append(temp)
    return articles
        

def main():
#     # apiKey = 
    response = makeCallEverything(apiKey, 'united nations', 'content')
    if response == None:
        print("1")
    for article in response:
        print(article.title)
        #what do we want to do in case API throws exception?
    #transport objects to database from here
    


if __name__ == '__main__':
    main()






    

