import json
import os
import requests

from bs4 import BeautifulSoup

dir_path = os.path.dirname(os.path.realpath(__file__))


def crawlDataCovidVn():
    try:
        linkNews = "https://covid19.gov.vn"
        responseNews = requests.get(linkNews)
        soup = BeautifulSoup(responseNews.content, "html.parser")
        titles = soup.findAll('a', class_="img-resize")

        linkCovidNum = "https://static.pipezero.com/covid/data.json"
        responseCovidNum = requests.get(linkCovidNum)

        if len(titles) == 0 or responseCovidNum == {}:
            raise Exception("error from api")

        response = {
            "news": [],
            "covidNum": responseCovidNum.json()
        }

        for item in titles:
            response["news"].append({
                'link': linkNews + item['href'],
                'title': item['title'],
                'image': item.findChild("img")["src"]
            })
        return response
    except:
        print("send default res")
        with open(os.path.join(dir_path, 'defaultRespone.txt'), "r") as filehandle:
            response = json.load(filehandle)
        return response

