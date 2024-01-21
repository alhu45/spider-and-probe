#https://en.wikipedia.org/wiki/Programmer

# Web Spidering, also known as Web indexing is a method to index context of websites
# by searching browsing World Wide Web. The purpose of web crawling is to provide up to date
# information in search results. Google and other search engines use web crawling in order
# to provide updated results.

#Scrapes all the urls in the website inputted

import requests
from bs4 import BeautifulSoup

#function to get url
def get_page(url):
    #gets requested https
    response = requests.get(url)

    #pulls out data from the html and xml files
    soup = BeautifulSoup(response.content, 'html.parser')

    #finds all the lines with the anchor (<a>) tags in the html content
    tag = soup.findAll("a")

    #finds the title of the html content
    #print(soup.title.string)

    #finds all the tags
    #tag = soup.find_all("a")
    #print(tag)

    #find all hrefs in the html content
    for t in tag:
        url2 = t.get("href")
        print(url2)


get_page(input("What URL would you like to scrape? "))


