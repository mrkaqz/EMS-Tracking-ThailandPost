#Python code to track package from Thailand Post
import requests
import json
import urllib3

#Disable InsecureRequestWarning 
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

#read token
from dotenv import load_dotenv
load_dotenv()
import os

#get token from .env file
tokenKey = os.getenv('Token')

inputOK = True

#input for tracking number
while inputOK:
    #asking for the tracking number
    barcode = input('Traking Number: ')
    #barcode = 'EF582568151TH'
    if len(barcode) == 13:
        inputOK = False
    else:
        print('Please enter correct tracking number')



#server address of Thailand Post
serverAddress = 'https://trackapi.thailandpost.co.th/post/api/v1/'


trackAddress = serverAddress + 'track'
tokenAddress = serverAddress + 'authenticate/token'

#POST content to get token
headers    = {'Content-Type': 'application/json',
            'Authorization': 'Token '+tokenKey}

#POST to HTTP Address to get token
responseToken = requests.post(tokenAddress, headers=headers, verify=False, timeout=300)


#POST results for token
resultsToken = responseToken.json()
getToken = resultsToken['token']
#print(getToken)


#POST content to track package with result from get token.
headers    = {'Content-Type': 'application/json',
            'Authorization': 'Token '+getToken}

body  = {   "status": "all",
            "language": "TH",
            "barcode": [barcode]
        }       

#POST to HTTP Address to track package
response = requests.post(trackAddress, headers=headers, data=json.dumps(body), verify=False)

results = response.json()

line = results['response']['items'][barcode]

#output result
for i in range(len(line)):
    for key,val in line[i].items():
        print(key,':',val)
    print('------------------------')