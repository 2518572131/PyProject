#字典的操作都基于[],[]是查找存放键值得

score={'张三':'90','李四':'98','李四':'92'}
print(score)
print("张三" in score)
print('李四' not in score)
print('王五'in score)


#删除
del score['李四']
print(score)

#新增
score['陈六']=90
print(score)