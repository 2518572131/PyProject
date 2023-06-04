#利用index（）函数获取列表的索引，当列表中有相同元素时，会返回第一个元素的索引
#当检索的元素不存在列表中，则会返回ValueError,即报错

lst=['hello','python','word',98,'hello']

print(lst[0:5])
print(lst[:4])
print(len(lst))
print(98 in lst)
print(99 not in lst)
for item in lst:
    print(item)


#添加元素
print(id(lst))
#append在列表的末尾至少添加一个元素
lst.append('OK')
print(lst)
print(id(lst))

lst2=[12,14]
lst.append(lst2)
print(lst)  #结果是['hello', 'python', 'word', 98, 'hello', 'OK', [12, 14]]
print(id(lst))

lst.extend(lst2)
print(lst) #结果是['hello', 'python', 'word', 98, 'hello', 'OK',  12, 14]
print(id(lst))
#append和extend的区别是append添加一个列表时，是将这个列表作为一个元素添加的；但是extend是分别作为一个元素添加的


#在任何一个位置上添加一个元素，用insert
lst.insert(1,"nihao")
print(lst)
print(id(list))

#切片：在任意位置添加N多个元素；切掉原有的元素，用新的元素去替代
lst3=['bye','goodbye']
lst[1:]=lst3
print(lst)
print(id(lst))
