answer=input('你是会员吗?y/n')
money=float(input('请输入你的购物金额:'))

if(answer=='y'):
    if(money>=200):
        print('可以打八折，付款金额为：',money*0.8)
    elif money>=100:
        print('可以打九折，付款金额为：',money*0.9)
    else:
        print('不可以打折')

else:
    if(money>=200):
        print('可以打九折，付款金额为：',money*0.9)
    elif money>=100:
        print('可以打九五折，付款金额为：',money*0.95)
    else:
        print('NO')