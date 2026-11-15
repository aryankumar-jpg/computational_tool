import requests
from bs4 import BeautifulSoup

url = input("Enter URL (default https://news.ycombinator.com/): ")
if not url:
    url = "https://news.ycombinator.com/"

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

items = soup.find_all('span', class_='titleline')
for item in items:
    link_tag = item.find('a')
    if link_tag:
        print("Title:", link_tag.text)
        print("Link:", link_tag['href'])
        print("-" * 40)
