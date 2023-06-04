import xlrd

import re
from collections import Counter
import  matplotlib.pyplot as plt

from queue import Queue

file_path1 = xlrd.open_workbook("454.xls")
sh1 = file_path1.sheet_by_index(0)
list1 = []
last2 = []
last3 = []
last4 = []
lst5 = set()
last6 = []
last7  = []

for i in range(600):
    list1.append(sh1.cell_value(i + 1, 0))
for i in list1:
    try:
        b = i.replace("-", "")
        #  c = re.findall(",\d+[0,20]\d+",b)
        #  d = c[1]
        bbb = re.findall(",\d+\,[\s\S]*", b)
        ccc = bbb[0].replace(",", "")
        ddd = re.findall("\d+[0,20]\d+", ccc)
        last2.append(bbb[0].replace(ddd[0], "").replace(",", ""))

    except:
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++")
for i in last2:
    vvv = re.findall("\d+[6,100]\d+", i)
    last4.append(i.replace(vvv[0], ""))
yyyy = Counter(last4)
d = sorted(yyyy.items(), key=lambda x: x[1], reverse=True)
plt.style.use("ggplot")
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']

for i in range(10):
    last6.append(d[i][0])
    last7.append(d[i][1])
print(last6)
print((last7))
bar_wridth = 0.5
plt.bar(last6,last7,width = bar_wridth)
plt.xticks(rotation=20)
x_range = range(10)
for xx,yy in zip(x_range,last7):
    plt.text(xx - bar_wridth / 20 ,yy+1,yy,ha = 'center',fontsize = 10)
plt.title("前十名作者对应的歌单")
plt.xlabel("作者")
plt.ylabel("歌单数")
plt.show()



