import sys
sys.path.append('/tmp/locust/common')
import yaml

def read_token():
    file = open(r'token.yaml','r')
    data = yaml.load(file, Loader=yaml.FullLoader)
    print(data)
    return data
if __name__ =="__main__":
     read_token()