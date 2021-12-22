import requests
from config.config import url

def oauth_pass():
    Url = "/oauth/phone"
    Data = {'username': "13537700044", 'password': "e9bc0e13a8a16cbb07b175d92a113126",'client':"web"}
    Headers = {'Content_type': "application/json"}
    rep = requests.post(Url, Data, Headers)
    return rep.json()['data']['accessToken']

if __name__ == "__main__":
    oauth_pass()
