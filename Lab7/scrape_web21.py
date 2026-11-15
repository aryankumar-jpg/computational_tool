import requests
from bs4 import BeautifulSoup
import csv

url = input("Enter URL (default https://books.toscrape.com/): ")
if not url:
    url = "https://books.toscrape.com/"

filename = input("Enter output CSV filename (default books.csv): ")
if not filename:
    filename = "books.csv"

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

books = soup.find_all('article', class_='product_pod')

with open(filename, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Price"])
    for book in books:
        title = book.find('h3').find('a')['title']
        price = book.find('p', class_='price_color').text
        writer.writerow([title, price])

print("Data successfully scraped and saved to", filename)
