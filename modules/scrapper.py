from bs4 import BeautifulSoup
import requests

def scrapper(url):
    preffered_blogging_site = url
    source = requests.get(preffered_blogging_site).text


    soup = BeautifulSoup(source,'xml')

    section = soup.find("section")

    headline = section.h1.span.text




  
    return headline

