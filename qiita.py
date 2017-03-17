from bottle import get, post, run
from bottle import request, template, redirect
import requests
import json

url = "http://qiita.com/api/v2/items"
data = requests.get(url).json()

@get('/')
def get_qiita():
    articles = []
    for article in data:
        articles.append(dict(title=article["title"],
                         user_id=article["user"]["id"],
                         user_image=article["user"]["profile_image_url"],
                         url=article["url"]
                         ))
    return template('index.tpl', articles=articles)
if __name__ == "__main__":
    run(host='192.168.33.10', port=8080, debug=True, reloader=True)
