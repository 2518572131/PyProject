#银行卡输入密码，次数为3次
for i in range(3):
    pwd=input('请输入密码:')

    if pwd=='8888':
        print('密码正确')
        break
    else:
        print('密码错误')
        




#输出一盒3行4列的矩形，外层控制行数，内层控制列数
for i in range(3):
    for j in range(4):
        print('*',end='\t')
        j=j-1
    print()
