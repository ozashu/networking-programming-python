from bottle import get, post, run
from bottle import request, template, redirect
import requests

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

@post('/')
def search_qiita():
    article_title = []
    searched_user_id = []
    keyword = request.forms.get('keyword')

    for article in data:
        search_article = dict(title=article["title"],
                            user_id=article["user"]["id"],
                            user_image=article["user"]["profile_image_url"],
                            url=article["url"]
                            )
        if keyword in article['title']:
            article_title.append(search_article)
        if keyword in article['user']['id']:
            searched_user_id.append(search_article)

    return template('search_result.tpl', keyword=keyword,article_title=article_title,searched_user_id=searched_user_id)

if __name__ == "__main__":
    run(host='192.168.33.10', port=8080, debug=True, reloader=True)
