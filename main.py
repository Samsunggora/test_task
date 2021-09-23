import requests
from bs4 import BeautifulSoup
import sqlite3

url = "https://www.csfd.cz/zebricky/filmy/nejlepsi/?showMore=1"
headers = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:92.0) Gecko/20100101 Firefox/92.0"
}
req = requests.get(url, headers=headers)
src = req.text
# print(src)
# with open("index.html", "w") as file:
#     file.write(src)
with open("index.html") as file:
    open_file = file.read()

soup = BeautifulSoup(src, "lxml")
all_products_hrefs = soup.find_all(class_="article-content article-content-toplist")

page_find_1 = soup.find_all(class_="film-title-user")
for item1 in page_find_1:
    print(item1.text.strip())

page_find_2 = soup.find_all("a", class_="film-title-name")
for item2 in page_find_2:
    print(item2.text.strip())

# page_find_3 = soup.find_all("p")
# for item3 in page_find_3:
#     print(item3.text.strip())
string_rezie = {}
page_find_3 = soup.find_all("div", class_="article-content article-content-toplist")
for item3 in page_find_3:
    item_text = item3.find_all("p")
    item_text1 = item_text

    print(item_text1)

    # soup = BeautifulSoup(html, "html.parser")
    # container = soup.select_one("div.column column-minus-300")
    # print(container)
    #
    #
    # src = req.text
    # print(src)
    # with open("index.html", "w") as file:
    #     file.write(src)
    #
    # with open("index.html") as file:
    #     src = file.read()
    #
    # all_categories_dict = {}
    # soup = BeautifulSoup(src, "lxml")
    # all_products_hrefs = soup.find_all(class_="film-title-name")
    # for items in all_products_hrefs:
    #     item_text = items.text
    #     item_href = "https://www.csfd.cz" + items.get("href")
    #     print(f"{item_text}: {item_href}")
    #     all_categories_dict[item_text] = item_href
