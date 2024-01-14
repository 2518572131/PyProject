#for循环
animals=['cat','pet','smilk','tigger']
for i in animals:
    if i !='tigger':
        print(i.title())
    else:
        print(i.upper())


#条件测试
animals='car'
print(animals=='car')
animals1=['cat','pet','smilk','tigger']
print('cat' in animals1)

car='subaru'
print("Is car=='subaru' ? i periced true")
print(car=='subaru')

print("Is car=='auid' ? t peried false")
print(car=='auid')


#if-elif-else
age=18
if age<4:
    price=0
elif age<19:
    price=5
else:
    price=10
print("zui hou shi is $"+str(price)+".")

#list[]
list=['cat']
if list:
    for i in list:
        print('you have a new food'+' '+i)
    print("OK")
else:
    print("you have must make food")