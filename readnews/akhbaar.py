from win32com.client import Dispatch
import json
import requests

def speak(str):
    spoke = Dispatch('SAPI.SpVoice')
    spoke.Speak(str)

if __name__ == "__main__":
    speak("News are as follows...")
    url = 'http://newsapi.org/v2/top-headlines?country=in&apiKey=66a2a77d17384c54ad972414b54eee09'
    news = requests.get(url).text
    news_dict = json.loads(news)
    # print(news_dict["articles"])
    arti = news_dict['articles']
    for article in arti:
        print(article['title'])
        speak(article['title'])
        speak("The next news is ")


