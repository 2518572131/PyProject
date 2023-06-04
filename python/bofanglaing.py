import pandas as pd
from pyecharts.charts import Pie  #画饼图
from pyecharts.charts import Bar  #画柱形图
from pyecharts import options as opts
import matplotlib.pyplot as plt

# 读入数据，需要更改
#可视化
data = pd.read_csv('kugou.csv')
#根据播放量排序，只取前十个
df = data.sort_values('playcount',ascending=False).head(10)
print("-----"*15)
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
bar = (
    Bar()
    .add_xaxis(df['specialname'].values.tolist())
    .add_yaxis('播放量排名前十对应的收藏量', df['collectcount'].values.tolist(),itemstyle_opts=opts.ItemStyleOpts(color="green"))
    
)


bar.render("E://条形图.html")
print("柱形图保存成功！")


