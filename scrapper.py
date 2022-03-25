import requests
response = requests.get("https://www.ceneo.pl/63490289#tab=reviews")
print(response.status_code)
