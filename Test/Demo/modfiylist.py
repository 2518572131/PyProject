lst=[1,2,3,4,5,6,7,8,9]
#修改一个列表中的一个元素
lst[2]=10
print(lst)
#一次修改多个值
lst[1:3]=[11,12,13]
print(lst)

#将元素列表反向
lst.reverse()
print(lst)

#统计一个元素出现的次数
print(lst.count(1))

#求元素的最大值和最小值
print(min(lst))
print(max(lst))


#利用sort()函数进行排序
lst.sort()
print(lst)#默认升序
lst.sort(reverse=True)
print(lst)


#利用for循环生成一个列表序列
lst1=[i for i in range(10)]
print(lst1)

#列表中的元素生成2-4-6-8-10
lst2=[i*2 for i in range(1,6)]
print(lst2)