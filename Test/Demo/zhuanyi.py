#转义字符的使用


print('hello\nword')  #换行符
print('hello\tword')  #空格符，一个\t是4位
print('hello\rword')  #word将hello进行了覆盖
print('hello\bword')  #是一个退格符，将o给退掉了

#输出网址
print(':\\\\baidu.com')
print('老师说：\'大家好\'')  #'是特殊符号，想要输出'号需要转义字符转义


#原字符-----让转义字符失效，利用r或者R
print(r'hello\nword')