from flask import Flask, request, render_template, redirect, session
import requests

app = Flask(__name__)

url = "http://qiita.com/api/v2/items"
data = requests.get(url).json()

@app.route('/')
def get_qiita():
    """Get newest Qiita Articles
    """
    articles = []
    for article in data:
        articles.append(dict(title=article["title"],
                         user_id=article["user"]["id"],
                         user_image=article["user"]["profile_image_url"],
                         url=article["url"]
                         ))
    return render_template('index.html', articles=articles)

@app.route('/', methods=['POST'])
def search_qiita():
    """Serch newest Qiita Articles
    """
    searched_result = [] # empty list
    keyword = request.form['keyword'] # Get form Keyword

    for article in data:
        search_article = dict(title=article["title"],
                            user_id=article["user"]["id"],
                            user_image=article["user"]["profile_image_url"],
                            url=article["url"]
                            )
        if keyword in search_article['title']:
            searched_result.append(search_article)
        if keyword in search_article['user_id']:
            searched_result.append(search_article)

    return render_template('search_result.html', searched_result=searched_result)

if __name__ == '__main__':
    app.run(host=localhost,debug=True)
