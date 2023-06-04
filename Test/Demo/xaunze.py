money=1000
a=int(input('请输入取款金额：'))
if(a<=money):
    print('可以取款,余额为:',money-a)
    money=money-a
else:
    print('不可以取款')
