#Scrapes the website and finds all the url with the keyword in it

from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup
from urllib import *

#identifies all individual urls and will delete duplicates
visited_urls = set()

#passes a keyword in the url to find the url with the selected keywords
def spider_url (url, keyword):
    try:
        #gets requested https
        response = requests.get(url)
    except:
        print(f"Error. Requested failed {url}")
        return

    if response.status_code == 200:
        #pulls out data from the html and xml files
        soup = BeautifulSoup(response.content, 'html.parser')

        #finds all the anchor tags
        anchor_tag = soup.find_all('a')

        #stores url in lisw
        urls = []

        #find all hrefs in the html content
        for tag in anchor_tag:
            href = tag.get("href")

            #appends href if it is not empty
            if href is not None and href != "":
                urls.append(href)

            #print(urls)

        #removes duplicates of urls, recursively calls it and searches for the keyword
        for url2 in urls:
            if url2 not in visited_urls:
                visited_urls.add(url)
                url_join = urljoin(url, url2)
                if keyword in url_join:
                    print(url_join)
                    spider_url(url_join, keyword)
            else:
                pass


url = input("Enter the url you want to scrape: ")
keyword = input("Enter the keyword to search for in the url: ")
spider_url(url, keyword)

