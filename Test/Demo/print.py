#将结果以文件形式输出
#先给上文件的路径，利用a+表示路径中没有该文件则首先创建文件，有文件就在文件内容的后面追加
#然后将文件赋值给变量，利用print输出,在输出语句中需要将变量值赋值给文件值
#对于文件的操作在结尾处需要关闭文件

fp=open('D:/txt.txt','a+')
print('helloword',file=fp)
fp.close()


#不换行输出
print('hello','word','pyrthon')