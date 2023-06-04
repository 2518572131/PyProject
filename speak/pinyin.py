from pypinyin import pinyin, lazy_pinyin, Style
import numpy as np
import re

def trans_aishell_to_pinyin(word_path, pinyin_path):
	# 需要转换为拼音的中文汉字路径
	textobj = open(word_path, 'r+', encoding='UTF-8')
	# 转化为拼音后的保存txt路径
	savefile = open(pinyin_path, 'w+', encoding='UTF-8')
	# 对aishell进行文本数据处理
	for x in textobj.readlines():
		textlabel = x.strip('\n')
		textlabel = textlabel.split(' ')
		x = pinyin(textlabel,style=Style.TONE3)
		print(x)
		str2 = ''
		for i in x:
			str1 = " ".join(i)
			if (re.search(r'\d',str1)):
				pass
			else:
				str1 += '5'
			str2 = str2 + str1 + ' '
		str2 = str2[:-1]
		# 保存生成的数据
		savefile.write(str2 + "\n")
#1.txt放自己的汉字，2.TXT会生成对应拼音序列
trans_aishell_to_pinyin("1.txt","2.txt")