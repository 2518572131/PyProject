#list
list=['lili','liuhai']
print(list[-1])
#append()
list.append('lili')
print(list)
#insert
list.insert(1,'love')
print(list)
#del
del list[1]
print(list)
#pop,获取列表最后一个元素，亦可以下角标指定
pop_list=list.pop()
print(pop_list)
print(list)
#pop和del的区别:pop删除后会暂存，还可以继续使用，但是del彻底删除
#remove
list.remove('lili')
print(list)
#sort,永久排序
list1=['cat','duck','apple','sb']
list1.sort()
print(list1)
#倒叙
list1.sort(reverse=True)
print(list1)
#sorted临时排序
list2=['cat','duck','apple','sb']
print(sorted(list2))
print(list2)
#倒叙
list2.reverse()
print(list2)
print(list2)
#len()
print(len(list2))

#for,遍历list2中的值并将其存储在listss
for listss in list2:
    print('this is a good '+listss+"!")
    print('i love'+" "+listss)

print(listss+"is people's friend")

#range()
for i in range(1,5): 
    print(i)
#
#numbers = list(range(1, 6))
#print(numbers)

#创造数字
list3=[]
for i in range(1,11):
    list3.append(i*i)
print(list3)
#min,max
print(min(list3))
print(max(list3))
print(sum(list3))

#列表解析
list4=[i**2 for i in range(1*11)]
print(list4)

#copy,这种是新建一个列表，使用list的话是用同一个索引，其中一个改变，另一个也会改变
friend=['1','2']
print(friend)
me=friend[:]
print(me)