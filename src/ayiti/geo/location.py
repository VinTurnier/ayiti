# coding=utf-8
import json, ast
import requests
from bs4 import BeautifulSoup

class Location:

    def __init__(self,arrondissement="Port-au-Prince"
                ,base_url="https://fr.wikipedia.org/wiki/"):
        
        page = requests.get(base_url+arrondissement)
        soup = BeautifulSoup(page.content,"html.parser")
        result = soup.find(class_="infobox_v2")
        self.data = result.find("tbody")

        self.arrondissement_info = {}
    
    def info(self):
        for r in self.data.find_all("tr"):
            table_header = r.find("th")
            table_data = r.find("td")

            if table_header and table_data:
                table_header_split = table_header.text.split("\n")
                table_data_split = table_data.text.split("\n")
                self.arrondissement_info[table_header_split[0]\
                        .encode("utf-8")] = table_data_split[0]\
                        .encode("utf-8")
        return self.arrondissement_info


if __name__ == "__main__":

    a = Location(arrondissement="Pétion-Ville")
    print(a.info())