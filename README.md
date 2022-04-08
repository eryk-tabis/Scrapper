# Scrapper

##Struktura opinii w serwisie Ceneo [Ceneo.pl](https://www.ceneo.pl/)

|Składowa|Selektor|Nazwa zmiennej|Typ zmiennej|
|--------|--------|--------------|------------|
|opinia|div.js_product-review|opinion|bs4.element.Tag|
|indentyfikator opinii|div.js_product-review["data-entry-id"\]|opinion_id|str|
|autor opinii|span.user-post__author-name|author|str|
|rekomendacja|span.user-post__author-recomendation > em|recomendation|str|
|liczba gwiazdek|span.user-post__score-count|score|str|
|treść opinii|div.user-post__text|content|str|
|lista zalet|div.review-feature__title--positives ~ div.review-feature__item|pros|list|
|lista wad|div.review-feature__title--negatives ~ div.review-feature__item|cons|list|
|dla ilu osób przydatna|buttton.vote-yes > span|usefull|str|
|dla ilu osób nieprzydatna|buttton.vote-no > span|useless|str|
|data wystawienie opinii|span.user-post__published > time:nth-child(1)["datetime"]|published|str|
|data zakupu|span.user-post__published > time:nth-child(2)["datetime"]|bought|str| 