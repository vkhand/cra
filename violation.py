import bs4
import requests
import json
import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/api', methods=['GET'])
def crawler():


    vehical_no = request.args.get('vehicleNo')
    s=requests.Session()
    payload = {'SearchBy':'REGNO',
                'SearchValue': vehical_no,
                'ServiceCode': 'BPS'}
    page = requests.post("https://www.karnatakaone.gov.in/PoliceCollectionOfFine/FineDetails?SearchBy=REGNO&SearchValue="+str(vehical_no)+"&ServiceCode=BPS", data=payload)
    soup = bs4.BeautifulSoup(page.text,"html.parser")
    d=json.loads(str(soup))
    return jsonify(d)
    
if __name__=="__main__":
    app.run()
	
	


