#coding:utf-8
import json
import operator
class CommonUtil:
	def is_contain(self,str_one,str_two):
		'''
		判断一个字符串是否在另外一个字符串中
		str_one:查找的字符串
		str_two：被查找的字符串
		'''
		flag = None
		if isinstance((str_one,str_two),str):
			str_one = str_one.encode('unicode-escape').decode('string_escape')
			str_two = str_two.encode('unicode-escape').decode('string_escape')
		# return operator.eq(str_one,str_two)
		if str_one in str_two:
			flag = True
		else:
			flag = False
		return flag


	def is_equal_dict(self,dict_one,dict_two):
		'''
		判断两个字典是否相等
		'''
		if isinstance(dict_one,str):
			dict_one = json.loads(dict_one)
		if isinstance(dict_two,str):
			dict_two = json.loads(dict_two)
		# return cmp(dict_one,dict_two)
		return operator.eq(dict_one,dict_two)

if __name__ == '__main__':
	d = CommonUtil()
	dict_one = "{'a':'a1','b':1}"
	dict_two = "{'a':'a1','b':1}1"
	print(type(dict_one))
	dict_one1 = d.is_contain(dict_one,dict_two)
	print(dict_one1)