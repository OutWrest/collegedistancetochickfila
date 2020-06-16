import requests as re
from urllib.parse import urljoin
from bs4 import BeautifulSoup

class Scrape():
    def __init__(self, url):
        self.url = url
    
    def __sendRequest(self, endpoint=None, params=None, headers=None, timeout=None):
        return re.get(urljoin(self.url, endpoint), params=params, headers=headers, timeout=timeout)

    def scrape(self, endpoint, element, attrs=None, params=None, headers=None, timeout=None):
        req = self.__sendRequest(endpoint, params, headers, timeout)
        #print(req)
        if req.status_code == 200:
            bs = BeautifulSoup(self.__sendRequest(endpoint, params, headers, timeout).text, 'html.parser')
            return bs.find_all(element, attrs=attrs)#.text
        return None