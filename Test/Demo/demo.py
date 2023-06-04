#range()函数的三种用法

#括号中只有一个数字时，就表示从0开始到数字的结束序列
r=range(10)
print(list(r))


#表示从头开始到尾结束，包含头但不包含尾
r=range(1,10)
print(list(r))

#表示从头开始到尾结束，包头不包尾，步长为2
r=range(1,10,2)
print(list(r))

'''用in或者not in判断某个数字是否在序列中'''
print(10 in r)
print(9 in r)
print(10 not in r)
print(9 not in r)