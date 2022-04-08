import requests
from bs4 import BeautifulSoup
response = requests.get("https://www.ceneo.pl/63490289#tab=reviews")
page = BeautifulSoup(response.text, 'html.parser')

opinions = page.select("div.js_product-review")
opinion = opinions.pop(3)
opinion_id = opinion["data-entry-id"]
author = opinion.select_one("span.user-post__author-name").get_text().strip()
recomendation = opinion.select_one("span.user-post__author-recomendation > em").get_text().strip()
score = opinion.select_one("span.user-post__score-count").get_text().strip()
content = opinion.select_one("div.user-post__text").get_text()
pros = [item.get_text() for item in opinion.select("div.review-feature__title--positives ~ div.review-feature__item")]
cons = [item.get_text() for item in opinion.select("div.review-feature__title--negatives ~ div.review-feature__item")]
usefull = opinion.select_one("button.vote-yes > span").get_text().strip()
useless = opinion.select_one("button.vote-no > span").get_text().strip()
publish_date = opinion.select_one("span.user-post__published > time:nth-child(1)")["datetime"]
purchase_date = opinion.select_one("span.user-post__published > time:nth-child(2)")["datetime"]
