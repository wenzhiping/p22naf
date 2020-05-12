#coding:utf-8
# import MySQLdb.cursors
import pymysql
import json
class OperationMysql:
	def __init__(self):
		self.connection = pymysql.connect(
			host='localhost',
			port=3306,
			user='root',
			passwd='888888',
			db='guest_test',
			charset='utf8',
			cursorclass=pymysql.cursors.DictCursor
			)
		# self.connection = self.connection.cursor()

	#查询一条数据
	def search_one(self,sql):
		self.connection = self.connection.cursor()
		self.connection.execute(sql)
		result = self.connection.fetchone()
		result = json.dumps(result)
		return result

	# def insert(self, table_name, table_data):
	# 	for key in table_data:
	# 		table_data[key] = "'" + str(table_data[key]) + "'"
	# 	key = ','.join(table_data.keys())
	# 	value = ','.join(table_data.values())
	# 	real_sql = "INSERT INTO " + table_name + " (" + key + ") VALUES (" + value + ")"
	# 	# print(real_sql)
    #
	# 	with self.connection.cursor() as cursor:
	# 		cursor.execute(real_sql)
    #
	# 	self.connection.commit()
    #
	# # close database
	# def close(self):
	# 	self.connection.close()
if __name__ == '__main__':
	op_mysql = OperationMysql()
	res = op_mysql.search_one("select * from sign_guest where realName='jktest'")
	print(res)
