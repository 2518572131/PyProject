#remove和list的区别，remove是一个方法，需要调用；但是del是一个函数，直接使用
#remove用的是元素，但是del用的是索引
lst=['hello','python','word',98,'hello',90,80]
lst.remove('hello')
print(lst)  #结果是['python', 'word', 98, 'hello']，有相同的元素时，会移除其中一个元素，从索引开始处移动

#利用索引移除元素，pop()函数
lst.pop(1)
print(lst)

#如果pop()函数中没有方参数，则会删除列表中的最后一个元素
lst.pop()
print(lst)


print('----------切片操作会得到一个新列表,是被切掉的部分-----------')
lst1=lst[1:3]
print(lst1)   #结果是[98, 'hello']，即得到的新列表是切掉的东西


#不得到一个新的列表
print('---------是切掉的保留部分------------')
lst[1:3]=[]
print(lst)

print('------------删除-----------')
lst2=[1,2,3,4,5,6,7,8,9]
del(lst2[0])
print(lst2)
print(id(lst2))

lst2.clear()
print(lst2)
print(id(lst2))

#删除整个列表
del lst2
print(lst2)