import requests
from bs4 import BeautifulSoup
import pandas as pd

proxies = {
    "http": "http://10.10.1.10:3128",
    "https": "https://10.10.1.10:1080"
}

data = {'Title': [], 'Price': []}
url = "https://www.amazon.in/s?k=iphone&crid=7TS7L3UAL0WC&sprefix=iphone%2Caps%2C210&ref=nb_sb_noss_1"

'''def fetchandsave(url, path):
    r=requests.get(url)
    with open(path, "w", encoding="utf-8") as f:
        f.write(r.text)

def getdata(url,path):
    with open("sample.html", "r", encoding="utf-8") as f:
        html_doc = f.read()

    soup = BeautifulSoup(html_doc, 'html.parser')


fetchandsave(url, "Data/iphones.html")
getdata(url, "Data/sample.html")'''

# python request to fake browser
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


r = requests.get(url, headers=headers)

soup = BeautifulSoup(r.text, 'html.parser')
# print(soup.prettify())
spans = soup.select("span.a-size-medium.a-color-base.a-text-normal")
prices = soup.select("span.a-price")

for span in spans:
    # print(span.string)
    data["Title"].append(span.string)

for price in prices:
    if not ("a-text-price" in price.get("class")):
        # print(price.find("span").get_text())
        data["Price"].append(price.find("span").get_text())
        if len(data["Price"]) == len(data["Title"]):
            break

df = pd.DataFrame.from_dict(data)
# df.to_csv("data.csv", index=False)
df.to_excel("data.xlsx", index=False)