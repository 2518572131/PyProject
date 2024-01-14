#字典{}
zidian={'name':'liudan','age':19,'sex':'女'}
zidian1={'name':'tangyuping','age':22,'sex':'女'}
print(zidian)
print(zidian['name'])
print(zidian1['name']) 
print(zidian.keys())
print(zidian1.values())

#添加键值对
zidian['name']='fjx'
zidian['age']=22
zidian['sex']='女'
print(zidian)

#{}
aline={}
aline['color']='green'
aline['point']=5
print(aline)

#update
aline_01={'color':'green'}
print(aline['color'])
aline_01['color']='yellow'
print(aline_01['color'])

#del
del zidian['sex']
print(zidian)

#遍历
for key,value in zidian1.items():#items() 是一个字典的方法，用于返回一个包含字典所有键值对的可迭代对象
    print("key:"+key)
    print("value:"+str(value))
for i in zidian.keys():
    print(i.title())

#去重
favorite_languages={
    'jesion':'python',
    'sarah':'C',
    'lili':'Java',
    'luxi':'python'
}
#不去重打印输出
#for languages in favorite_languages.values():
#   print(languages)

#去重
for languages in set(favorite_languages.values()):
    print(languages)
