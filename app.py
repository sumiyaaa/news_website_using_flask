from flask import Flask, render_template
from newsapi import NewsApiClient

app = Flask(__name__)


@app.route('/')
def index():
    newsapi = NewsApiClient(api_key="b47b9761cb6d4251b51cdd900de585c8")
    topheadlines = newsapi.get_top_headlines(sources="al-jazeera-english")

    articles = topheadlines.get('articles', [])

    news = []
    desc = []
    img = []

    for article in articles:
        news.append(article.get('title', 'No Title'))
        desc.append(article.get('description', 'No Description'))
        img.append(article.get('urlToImage', ''))

    mylist = zip(news, desc, img)

    return render_template('index.html', context=mylist)


if __name__ == "__main__":
    app.run(debug=True)
