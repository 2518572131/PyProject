score={'张三':'90','李四':'98','李四':'92'}
#不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住
print(score)
'''
dict.items()
以列表返回可遍历的(键, 值) 元组数组
'''
print(score.items())

'''
dict.keys()
以列表返回一个字典所有的键
'''
print(score.keys())
'''
dict.values()
以列表返回字典中的所有值
'''
print(score.values())