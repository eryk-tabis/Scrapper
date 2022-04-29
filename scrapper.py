import requests
import json
from bs4 import BeautifulSoup
item_id = input("Insert item id:\n")
url = f"https://www.ceneo.pl/{item_id}#tab=reviews"
all_opinions = []
while(url):
    response = requests.get(url)
    page = BeautifulSoup(response.text, 'html.parser')
    opinions = page.select("div.js_product-review")
    for opinion in opinions:
        opinion_id = opinion["data-entry-id"]
        author = opinion.select_one("span.user-post__author-name").get_text().strip()
        try:
            recomendation = opinion.select_one("span.user-post__author-recomendation > em").get_text().strip()
        except AttributeError:
            recomendation = None
        score = opinion.select_one("span.user-post__score-count").get_text().strip()
        content = opinion.select_one("div.user-post__text").get_text()
        pros = [item.get_text() for item in opinion.select("div.review-feature__title--positives ~ div.review-feature__item")]
        cons = [item.get_text() for item in opinion.select("div.review-feature__title--negatives ~ div.review-feature__item")]
        usefull = opinion.select_one("button.vote-yes > span").get_text().strip()
        useless = opinion.select_one("button.vote-no > span").get_text().strip()
        publish_date = opinion.select_one("span.user-post__published > time:nth-child(1)")["datetime"]
        try:
            purchase_date = opinion.select_one("span.user-post__published > time:nth-child(2)")["datetime"]
        except TypeError:
            purchase_date = None
        single_opinion = {
            "opinion_id": opinion_id,
            "author": author,
            "recomendation": recomendation,
            "score": score,
            "pros": pros,
            "cons": cons,
            "usefull": usefull,
            "useless": useless,
            "publish_date": publish_date,
            "purchase_date": purchase_date
        }
        all_opinions.append(single_opinion)
    try:
        url = f"https://www.ceneo.pl/{item_id}" + page.select_one("a.pagination__next")["href"]
    except TypeError:
        url = None
with open(f"opinions/{item_id}.json", 'w', encoding="UTF-8") as jf:
    json.dump(all_opinions, jf, indent=4, ensure_ascii=False)
