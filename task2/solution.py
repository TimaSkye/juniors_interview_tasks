import requests
from bs4 import BeautifulSoup
import csv

url = "https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту"
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
    'Referer': 'https://ru.wikipedia.org/'
}

beasts_count = {}


def parse_page(url):
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    categories = soup.find_all('h2', class_='mw-headline')

    for category in categories:
        category_text = category.text.strip()
        if category_text and category_text.isalpha():
            beasts_count[category_text] = beasts_count.get(category_text, 0)
    pages = soup.find_all('a')
    for page in pages:
        page_text = page.text.strip()
        if page_text and page_text.isalpha():
            beasts_count[page_text] = beasts_count.get(page_text, 0) + 1
    next_page_link = soup.find('a', rel='следующая страница')
    if next_page_link:
        next_page_url = 'https://ru.wikipedia.org' + next_page_link['href']
        parse_page(next_page_url)


parse_page(url)

with open('beasts.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Буква", "Количество"])  # Заголовок
    for letter, count in beasts_count.items():
        writer.writerow([letter, count])