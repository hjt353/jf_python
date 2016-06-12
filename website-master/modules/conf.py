#coding:utf8

#hjt353@qq.com  Jfpython@2016
#db info
db_user="jfpython"
db_password="jfedu.net"
db_host="192.168.100.8"
db_port=3306
db_name="jfpython"
db_charset="utf8"

'''
#1-100 user login reg error
#101-200 db error
#201-300 user_admin error 
'''
_code = {
	0:{"code":0,"message":"success"},
	1:{"code":1,"message":"please you give a post method"},
	2:{"code":2,"message":"user or password error"},
	3:{"code":3,"message":"The two passwords do not match"},
	4:{"code":4,"message":"please you change you phone number"},
	5:{"code":5,"message":"号码已存在"},
	6:{"code":6,"message":"号码不存在"},
	7:{"code":7,"message":"用户未激活"},
	101:{"code":101,"message":"db connection error"},
	103:{"code":103,"message":"db query error"}
	201:{"code":201,"message":"是管理员"}
	202:{"code":202,"message":"没有管理员权限"}
	203:{"code":203,"message":"管理员权限锁定"}
}
