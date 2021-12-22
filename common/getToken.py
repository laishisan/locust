import sys
sys.path.append('/tmp/locust/common/')
import yaml
import requests
from ruamel import yaml

class Token():
    def __init__(self):
        self.Url = "https://uat.pxxtech.com/oauth/pass"
        self.Data = {'username': "13612902987", 'password': "45ab18e58e7eb1b48f6d52b76aecaca9",'client':"web"}
        self.Headers = {'Content_type': "application/json"}
    def get_token(self):
       Url = self.Url
       data = self.Data
       headers = self.Headers
       rep = requests.post(Url, data, headers)
       return rep.json()['data']['accessToken']

    def write_token(self):
        tonken = self.get_token()
        yamlpath = r'/Token.yaml'
        with open(yamlpath, "w", encoding="utf-8") as f:
            yaml.dump(tonken, f, Dumper=yaml.RoundTripDumper)

if __name__=='__main__':
    Token().write_token()



