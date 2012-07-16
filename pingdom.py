#!/usr/bin/python
import requests, json
from requests.auth import HTTPBasicAuth

# define your pingdom account details
pingdom_url = "https://api.pingdom.com/api/2.0/checks"
pingdom_username = "CHANGEME"
pingdom_password = "CHANGEME"
headers = {'App-Key': 'CHANGEME'}
# Names of each check you ant to place on the dash
mychecks=['Check 1', 'Check 2', 'Check 3' ]

r = requests.get(pingdom_url, headers=headers, auth=HTTPBasicAuth(pingdom_username, pingdom_password))
data=r.json

# example HTML 
print '<H1 style= "margin:10px; padding:10px; font-size:56px; color: white; background-color: purple; font-family: Arial, sans-serif; text-align: center;">Page Speed</H1>' 
for items in data['checks']:
    if items['status'] == 'down':
        myback = 'red'
    if items['status'] == 'up':
        myback = 'green'
    if items['name'] in mychecks:
        myname = items['name']
        mytime = items['lastresponsetime']  
        print '<H1 style= "margin:1px; padding:5px; font-size:56px; color: white; background-color: %s; font-family: Arial, sans-serif; text-align: center;">%s %sms</H1>' % (myback, myname, mytime)
