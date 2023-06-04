a=1.1
b=2.2
print(a+b)
#结果是3.3000000000000003，浮点数计算不稳定


#数据类型转换
name="张三"
age=18
print('我是'+name+'，今年'+str(age)+'岁')


print('--------------利用str()将其余类型转换为str类型--------')
a=12
b=1.3415
c=False
print(type(a),type(b),type(c))
print(str(a),str(b),str(c),type(str(a)),type(str(b)),type(str(c)))



print('--------------利用float()将其余类型转换为float类型--------')
a=1
b=False
c='123' 
#d='hello'
print(type(a),type(b),type(c))
print(float(a),float(b),float(c),type(float(a)),type(float(b)),type(float(c)))