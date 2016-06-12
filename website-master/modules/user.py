#coding:utf8

import conf
import db
import hashlib
import sys
reload(sys)
sys.setdefaultencoding("utf8")

class User:
    def __init__(self):
        pass

    def user_esxits_status(self,phone):
        user = db.SQLdb()
        db_result = user.get_connection()
        if db_result:
            conn,cursor = db_result
            query = 'SELECT status FROM jf_user \
                                 WHERE phone="{phone}"'.format(phone=phone)
            if cursor.execute(query):#号码检测
                result = conf._code[5]#存在
                status = cursor.fetchone()[0]
                result["status"]=status
            else:
                result = conf._code[6]#不存在
            result["data"] = conn,cursor
            return result
        else:
            return conf._code[101]

    def phone_check(self,phone):
        if phone.isalnum() and len(phone) == 11: #11 number
            return True
        else:
            return False

    def user_login(self,phone,password):
        if not self.phone_check:
            return conf._code[4]

        db_result = self.user_esxits_status(phone=phone)
        if db_result["code"] == 5:#号码存在
            if db_result["status"] != 1:
                return conf._code[7]
            conn,cursor = db_result["data"]
            query = 'SELECT password FROM jf_user \
                                 WHERE phone="{phone}"'.format(phone=phone)
            try:          
                if cursor.execute(query):
                    db_password = cursor.fetchone()[0] #(("password"),("password"))
                    cursor.close();conn.close()
                    if db_password == hashlib.md5(password).hexdigest():
                        return conf._code[0]
                    else:
                        return conf._code[2] #password error
                else:
                    cursor.close();conn.close()
                    return conf._code[2] #user esxits
            except Exception, e:
                cursor.close();conn.close()
                result = conf._code[101]
                result["message"]=e
                return result
        else:
            return db_result
    
    def user_reg(self,phone,username,password,ensure_password,stage_class):
        if not self.phone_check:
            return conf._code[4]
            
        if password == ensure_password:
            db_result = self.user_esxits_status(phone=phone)
            if db_result["code"] == 6:
                conn,cursor = db_result["data"]
                query = 'INSERT INTO jf_user(phone,username,password,stage_class) \
                            VALUES("{phone}","{username}",md5("{password}"),"{stage_class}")'.format(phone=phone,
                                                                                     username=username,
                                                                                     password=password,
                                                                                     stage_class=stage_class)
                try:
                    cursor.execute(query)
                    conn.commit()
                    cursor.close();conn.close()
                    return conf._code[0]
                except Exception, e:
                    cursor.close();conn.close()
                    result = conf._code[101]
                    result["message"] = e
                    return result

            else:
                return db_result
        else:
            return conf._code[3]

    
    def check_admin(self,phone_id):
        '''
            check user Whether it is an administrator
        '''
        user = db.SQLdb()
        db_result = user.get_connection()
        if db_result:
            conn,cursor = db_result
            query = 'SELECT group_id FROM jf_admin \
                                 WHERE phone_id="{phone_id}"'.format(phone_id=phone_id)
            try:
                cursor.execute(query):#号码是否是管理员
                result = conf._code[201]# 是管理员
                statu = cursor.fetchone()[0]
                result['group_id'] = statu
            except Exception, e:
                result = conf._code[202]#不是管理员
            result["data"] = conn,cursor
            return result
        else:
            return conf._code[101]  

    def add_admin(self,phone_id):
        '''
        add a new one administrator
        '''
        db_result = self.check_admin(phone_id=phone_id)
        if db_result["code"] == 201:#是管理员
            #if db_result["status"] != 1: 暂时没有判断管理员权限是否锁定
            #    return conf._code[7]
            conn,cursor = db_result["data"]
            query = 'INSERT INTO jf_admin(phone_id,group_id) \
                            VALUES("{phone_id}",1)'.format(phone_id=phone_id)
            try:
                cursor.execute(query)
                conn.commit()
                cursor.close();conn.close()
                return conf._code[0]
            except Exception, e:
                cursor.close();conn.close()
                result = conf._code[101]
                result["message"]=e
                return result
        else:
            return db_result

    def delete_admin(self,phone_id):
        '''
        delete one administrator
        '''
        db_result = self.check_admin(phone_id=phone_id)
        if db_result["code"] == 201:#是管理员
            #if db_result["status"] != 1: 暂时没有判断管理员权限是否锁定
            #    return conf._code[7]
            conn,cursor = db_result["data"]
            query = 'DELETE  FROM jf_admin WHERE phone_id="{phone_id}"'.format(phone_id=phone_id)
            try:
                cursor.execute(query)
                conn.commit()
                cursor.close();conn.close()
                return conf._code[0]
            except Exception, e:
                cursor.close();conn.close()
                result = conf._code[101]
                result["message"]=e
                return result
        else:
            return db_result

    def show_entries(self,phone_id):
        '''
            select all user info
        '''
        db_result = self.check_admin(phone_id=phone_id)
        if db_result["code"] == 201:#是管理员
            #if db_result["status"] != 1: 暂时没有判断管理员权限是否锁定
            #    return conf._code[7]
            conn,cursor = db_result["data"]
            query = 'SELECT phone as "用户名", case group_id where 0 then "超级管理员" when 1 then "管理员" when 2 then "普通用户" end   FROM jf_python'
            try:
                cursor.execute(query)
                conn.commit()
                entries = [dict(phone=row[0], group_id=row[1]) for row in cursor.fetchall()]
                cursor.close();conn.close()
                return entries
            except Exception, e:
                cursor.close();conn.close()
                result = conf._code[101]
                result["message"]=e
                return result
        else:
            return db_result