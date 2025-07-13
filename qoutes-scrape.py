# Sample: scrape quotes
import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com"
soup = BeautifulSoup(requests.get(url).text, "html.parser")

for quote in soup.select(".quote"):
    text = quote.find("span", class_="text").text
    author = quote.find("small", class_="author").text
    print(f"{text} — {author}")
