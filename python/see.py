import pandas as pd
from pyecharts.charts import Pie  #画饼图
from pyecharts import options as opts
import matplotlib.pyplot as plt


# 读入数据，需要更改
#可视化
data = pd.read_csv("Kugou.csv")
#根据播放量排序，只取前十个
df = data.sort_values('playcount',ascending=False).head(10)
v = df['specialname'].values.tolist()   #tolist()将数据转换为列表形式
d = df['playcount'].values.tolist()
#设置颜色
color_series = ['#2C6BA0','#2B55A1','#2D3D8E','#44388E','#6A368B'
                '#7D3990','#A63F98','#C31C88','#D52178','#D5225B']
# 实例化Pie类
pie1 = Pie(init_opts=opts.InitOpts(width='1350px', height='750px'))
# 设置颜色
pie1.set_colors(color_series)
# 添加数据，设置饼图的半径，是否展示成南丁格尔图
pie1.add("", [list(z) for z in zip(v, d)],
        radius=["30%", "135%"],
        center=["50%", "65%"],
        rosetype="area"
        )
# 设置全局配置项
# TitleOpts标题配置项 
# LegendOpts图例配置项  is_show是否显示图例组件
# ToolboxOpts()工具箱配置项 默认项为显示工具栏组件

pie1.set_global_opts(title_opts=opts.TitleOpts(title='播放量top10歌单'),
                     legend_opts=opts.LegendOpts(is_show=False),
                     toolbox_opts=opts.ToolboxOpts())
# 设置系列配置项
# LabelOpts标签配置项  is_show是否显示标签；  font_size字体大小；
# position="inside"标签的位置，文字显示在图标里面； font_style文字风格
# font_family文字的字体系列
pie1.set_series_opts(label_opts=opts.LabelOpts(is_show=True, position="inside", font_size=12,
                                               formatter="{b}:{c}播放量", font_style="italic",
                                               font_weight="bold", font_family="Microsoft YaHei"
                                               ),
                     )
# 生成html文档
pie1.render("E:/玫瑰图.html")
print("玫瑰图保存成功！")

print("-----"*15)