import bs4
import requests
import json


def crawler(vehical_no):
    try:
        s=requests.Session()
        payload = {'SearchBy':'REGNO',
                   'SearchValue': vehical_no,
                    'ServiceCode': 'BPS'}
        page = requests.post("https://www.karnatakaone.gov.in/PoliceCollectionOfFine/FineDetails?SearchBy=REGNO&SearchValue=ka03mq9396&ServiceCode=BPS", data=payload)
        soup = bs4.BeautifulSoup(page.text,"html.parser")
        d=json.loads(str(soup))
        return d;
    except IndexError:
        return None

