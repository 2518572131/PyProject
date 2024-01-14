#使用用户输入来填充字典
responses={}
#设置一个标志，指出调查是否继续
flag=True

while flag:
    #提示输入被调差者的名字和回答
    name=input("\nWhat is your name")
    response=input("请输入今天是星期几:")
    #将答案存储在字典中
    responses[name]=response
    #看看还有多少人要参与调查
    repeat=input("(yes/no)")
    if repeat =='no':
        flag=False
print("------------")
for name,response in responses.items():
    print(name+" "+response+" ")
