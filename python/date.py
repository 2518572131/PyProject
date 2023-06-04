import time
import pandas as pd
import pyecharts as pye
import numpy as np
from pyecharts.charts import Bar  #画柱形图
from pyecharts import options as opts

def read_kugou(filepath:str):
    return pd.read_csv(filepath)

def tim():
    kugou = read_kugou("./kugou.csv")
    kugou["publishtime"] = pd.to_datetime(kugou["publishtime"])
    kugou=kugou.set_index("publishtime").sort_index(ascending=True)
    lis = pd.date_range(start="2021-05-01",end="2022-02-01",freq="M")
    ylis = []
    for i in range(len(lis)-1):
        count = np.array(kugou[lis[i]:lis[i+1]]["playcount"])
        ylis.append(np.max(count)/100000)
    bar = (
    Bar()
    .add_xaxis([f'{lis[i].strftime("%m")}-{lis[i+1].strftime("%m")}' for i in range(len(lis)-1)])
    .add_yaxis('每月最高歌单播放量/10万', ylis,itemstyle_opts=opts.ItemStyleOpts(color="#66ccff"))
    )
    bar.render("./每月最高播放量条形图.html")
    print("柱形图保存成功！")

    

if __name__ == "__main__":
    tim()