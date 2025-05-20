import requests
from bs4 import BeautifulSoup

web_url = "https://www.python.org/"

response = requests.get(web_url)
html_content = response.text
# print(html_content)

# buautify html with beautiful soup
soup = BeautifulSoup(html_content, "html.parser")

# get class named called medium-widget blog-widget
get_div = soup.find("div", class_= "medium-widget blog-widget")
# print(get_div)

# get h2 tag inside this div
get_h2 = get_div.find("h2")
print(get_h2.text)

# get the all li tag inside this div
get_li = get_div.find_all("li")

for li in get_li:
    print(li.text)