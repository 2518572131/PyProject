#字典和列表进行嵌套
student1={'name':'刘丹','age':12,'sex':'女'}
student2={'name':'刘阳','age':12,'sex':'女'}
list_student=[student1,student2]
print(list_student) 
for i in list_student:
    print(i)

#字典中存储列表
student3={
    'name':'lili',
    'project':['math','chinese','english']
}
print(student3['name']+' '+'favaruite projrct is'+' '+student3['project'][2 ])