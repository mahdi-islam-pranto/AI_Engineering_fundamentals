import requests
from bs4 import BeautifulSoup

url = "https://websockets.readthedocs.io/en/stable/index.html"

response =  requests.get(url)
# print(response.text)
html_content = response.text

# beautify the response
soup = BeautifulSoup(html_content, 'html.parser')
soup_html = soup.prettify()
# print(soup_html)

# find all the links in the page
links = soup.find_all('a')
for link in links:
    # print the href attribute of the link (a tag)
    print(link.get('href'))

# find all the h1 tags in the page
headlines = soup.find_all('h1')
for headline in headlines:
    print(headline.text)

# find all the p tags in the page
paragraphs = soup.find_all('p')
for paragraph in paragraphs:
    print(paragraph.text)


