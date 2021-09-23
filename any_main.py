import requests
from bs4 import BeautifulSoup
import json

url = "https://www.csfd.cz/zebricky/filmy/nejlepsi/?showMore=1"
headers = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:92.0) Gecko/20100101 Firefox/92.0"
}
req = requests.get(url, headers=headers)
src = req.text
print(src)
with open("index.html", "w") as file:
    file.write(src)

with open("index.html") as file:
    src = file.read()

all_categories_dict = {}
soup = BeautifulSoup(src, "lxml")
all_products_hrefs = soup.find_all(class_="film-title-name")
for items in all_products_hrefs:
    item_text = items.text
    item_href = "https://www.csfd.cz" + items.get("href")
    print(f"{item_text}: {item_href}")
    all_categories_dict[item_text] = item_href

with open("all_href.json", "w") as file:
    json.dump(all_categories_dict, file, indent=4, ensure_ascii=False)

with open("all_href.json") as file:
    all_categories = json.load(file)

for category_name, category_href in all_categories.items():

    rep = ["\n\t\t\t\t\t\t"]
    for items in rep:
        if items in category_name:
            category_name = category_name.replace(items, "")
print(all_categories)
print(category_name)
print(category_href)
