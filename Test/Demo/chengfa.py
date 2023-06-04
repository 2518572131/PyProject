#输出一盒3行4列的矩形，外层控制行数，内层控制列数
'''j=4
for i in range(3):
    while j>1:
        print('*',end='\t')
    print()
    j=j-1'''




#打印9*9乘法表
#行数为9行，一行打印一个；即内循环跟行数相等

for i in range(1,10):
    for j in range(1,i+1):
        print(i,'*',j,'=',i*j,end='\t')
    print()