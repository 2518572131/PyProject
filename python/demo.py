import pandas as pd
import numpy as np
from pyecharts.charts import Bar 
from pyecharts import options as opts
def get_max_gc(it=10):
    kugou=pd.read_csv("./kugou.csv")
    s = set(kugou["username"])
    lis = []
    for i in s:
        l=kugou[kugou["username"]==i]
        lis.append((i,len(l)))
    lis=sorted(lis,key=lambda x:x[1],reverse=True)
    return lis[:it]
def display(x,y):
    bar = (
    Bar()
    .add_xaxis(x)
    .add_yaxis('歌单数目', y,itemstyle_opts=opts.ItemStyleOpts(color="#6495ED"))
    )
    bar.render("./歌单创建数柱形图.html")
    print("柱形图保存成功！")

if __name__ == "__main__":
    x,y=tuple(zip(*get_max_gc()))
    display(x,y)
        
