import json
import requests
import datetime
import monthdelta
import math
f= open('showusers/apikeys.txt', 'r')
x=f.read().split('\n')

apikey= x[1]
apID= x[0]
def DateRecieve():
    date = datetime.date.today()-datetime.timedelta(days=1)
    if date.weekday() == 6:
        date = date-datetime.timedelta(days=2)
    elif date.weekday == 5:
        date = date-datetime.timedelta(days=1)
    return date

def UPorDOWN(first, second):
    index = str(math.fabs(round((first - second) / second * 100 , 1)) )
    if first>second:
        index=index + '%'
        tria='▲'
        color='green'
    elif first<second:
        index=index + "%"
        tria='▼'
        color='red'
    else:
        index = index + "%"
        tria = ''
        color='grey'
    return tria ,index, color

def AbrDay(date):
    x=str(date)
    a=x.split('-')
    mdate = datetime.datetime.strptime(str(a[1]), "%m").strftime("%b")
    return (mdate+" " +a[2])
    
def UsersAuth_DAY(date):
    headers = {
        'x-api-key': apikey ,
    }

    params = (
        ('query',
         'customEvents| where timestamp > startofday(datetime("' + str(
             date) + '")) and timestamp < endofday(datetime("' + str(
             date) + '"))| extend username1 = tolower(tostring(customDimensions.user))| distinct username1| count'),
    )

    response = requests.get('https://api.applicationinsights.io/v1/apps/'+ apID + '/query',
                            headers=headers, params=params)

    mydata = json.loads(response.text)
    value = mydata['tables'][-1]['rows'][-1][-1]
    
    return value, date


def UsersAuth_pDAY(date):
    date = date - datetime.timedelta(days=1)
    if date.weekday() == 6:
        date = date-datetime.timedelta(days=2)
    elif date.weekday == 5:
        date = date-datetime.timedelta(days=1)
    headers = {
        'x-api-key': apikey,
    }

    params = (
        ('query',
         'customEvents| where timestamp > startofday(datetime("' + str(
             date) + '")) and timestamp < endofday(datetime("' + str(
             date) + '"))| extend username1 = tolower(tostring(customDimensions.user))| distinct username1| count'),
    )

    response = requests.get('https://api.applicationinsights.io/v1/apps/'+ apID + '/query',
                            headers=headers, params=params)

    mydata = json.loads(response.text)
    value = mydata['tables'][-1]['rows'][-1][-1]
    return value

def UsersAuth_MON(date):
    end_date=date
    start_date=date - monthdelta.monthdelta(months=1)
    headers = {
        'x-api-key': apikey,
    }

    params = (
        ('query',
         'customEvents| where timestamp > endofday(datetime("' + str(
             start_date) + '")) and timestamp < endofday(datetime("' + str(
             end_date) + '"))| extend username1 = tolower(tostring(customDimensions.user))| distinct username1| count'),
    )

    response = requests.get('https://api.applicationinsights.io/v1/apps/'+ apID + '/query',
                            headers=headers, params=params)

    mydata = json.loads(response.text)
    value = mydata['tables'][-1]['rows'][-1][-1]
    return value, start_date, end_date


def UsersAuths_pMON(date):
    end_date = date - monthdelta.monthdelta(months=1)
    start_date = date - monthdelta.monthdelta(months=2)
    headers = {
        'x-api-key': apikey,
    }

    params = (
        ('query',
         'customEvents| where timestamp > endofday(datetime("' + str(
             start_date) + '")) and timestamp < endofday(datetime("' + str(
             end_date) + '"))| extend username1 = tolower(tostring(customDimensions.user))| distinct username1| count'),
    )

    response = requests.get('https://api.applicationinsights.io/v1/apps/'+ apID + '/query',
                            headers=headers, params=params)

    mydata = json.loads(response.text)
    value = mydata['tables'][-1]['rows'][-1][-1]
    return value

def Date_Today():
    date = datetime.date.today()
    return date
