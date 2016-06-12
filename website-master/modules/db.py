#coding:utf8
import MySQLdb
import conf

class SQLdb:
    def get_connection(self):
        try:
            conn = MySQLdb.connect(host=conf.db_host,
                                   user=conf.db_user,
                                   passwd=conf.db_password,
                                   db=conf.db_name,
                                   port=conf.db_port,
                                   charset=conf.db_charset)
            cursor = conn.cursor()
            return conn,cursor
        except Exception, e:
            return False


'''
id   0:超级管理员 1 :管理员  2；普通用户
status    1：被锁定  0：没锁定
#create table jf_admin(id int(10)  PRIMARY KEY NOT NULL UNIQUE AUTO_INCREMENT,\
#phone_id int NOT NULL,group_id int(10) NOT NULL,status int(1) NOT NULL default 0);

create table jf_group(id int(10)  PRIMARY KEY NOT NULL UNIQUE AUTO_INCREMENT,\
groupinfo char(20) NOT NULL,status tinyint NOT NULL default 0)

'''