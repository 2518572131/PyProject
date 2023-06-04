#利用zip函数将两个列表对象生成一个字典
items=['fruits','check','rice']
prices=['90','80','89']

d={item:price for item,price in zip(items,prices)}
print(d)