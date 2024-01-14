#input函数
messages=input('i love you')
print(messages)

i=1
while i <=5:
    print(i)
    i=i+1


promt="\ni will repeat it back to you:"
promt +="\nenter 'quit!'to end the progrem." 
message=''
while message !='quit!':
    message=input(promt)
    print(message)

    if message !='quit!':
        print(message)

#使用while删除重复元素
pets=['dog','cat','smilk','rabblit','cat','dog']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)