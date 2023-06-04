import json
from msilib.schema import PublishComponent
import requests
import pandas as pd


headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4495.0 Safari/537.36",
}

def get_html_text(url: str):
    """

    :param url:
    :return:
    """
    resp = requests.get(url, headers=headers)
    return resp.text
name = []
playc = []
collc = []
pubtime = []
username =[]
def decode_json(url:str):
    dict1 = json.loads(get_html_text(url))
    
    for dic in dict1["data"]["info"]:
        name.append(dic["specialname"])
        playc.append(dic["playcount"])
        collc.append(dic["collectcount"])
        pubtime.append(dic["publishtime"])
        username.append(dic["username"])


if __name__ == "__main__":
     for i in range(1,100):
         url =  f"http://mobilecdnbj.kugou.com/api/v3/tag/specialList?plat=0&page={i}&tagid=12&pagesize=30&ugc=1&id=68&sort=2"
         decode_json(url)
    
     dic3={"specialname":name,"playcount":playc,"collectcount":collc,"publishtime":pubtime,"username":username}
     pd.DataFrame(dic3).to_csv("kugou.csv")

    #x=pd.read_csv("kugou.csv")
    #pd.DataFrame(x).to_excel("kugou.xlsx")