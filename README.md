# Scrapper

##Struktura opinii w serwisie Ceneo [Ceneo.pl](https://www.ceneo.pl/)

|Składowa|Selektor|Nazwa zmiennej|Typ zmiennej|
|--------|--------|--------------|------------|
|opinia|div.js_product-review|user-post|obj|
|indentyfikator opinii|div.js_product-review["data-entry-id"\]|data_entry_id|int|
|autor opinii|span.user-post__author-name||||
|rekomendacja|span.user-post__author-recomendation > em|||
|liczba gwiazdek|span.user-post__score_count|user-post__score_count|string|
|treść opinii|div.user-post__text|user-post__text|string|
|lista zalet|div.review-feature__title--positives ~ div.review-feature__item|review-feature__col|obj|
|lista wad|div.review-feature__title--negatives ~ div.review-feature__item|||
|dla ilu osób przydatna|buttton.vote-yes > span|votes-yes-id|int|
|dla ilu osób nieprzydatna|buttton.vote-no > span|votes-no-id|int|
|data wystawienie opinii|span.user-post__published > time:nth-child(1)["datetime"]|user-post__published|list|
|data zakupu|span.user-post__published > time:nth-child(2)["datetime"]|user-post__published|list| 