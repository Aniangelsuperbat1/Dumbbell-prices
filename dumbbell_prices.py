import requests
from bs4 import BeautifulSoup as bs

source = requests.get(
    "https://www.amazon.com/s?k=35lb+dumbbells&ref=nb_sb_noss_2").text

soup = bs(source, "lxml")

prices = soup.find_all("span", class_="a-offscreen")
print(prices)
