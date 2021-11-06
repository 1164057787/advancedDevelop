from django.db import models



class User(models.Model):#用户表
    userid = models.CharField(max_length=32)  #主键
    username=models.CharField(max_length=32)
    password=models.CharField(max_length=32)#用id、昵称 密码


class Admin(models.Model):#管理员表，继承
    adminid=models.IntegerField(primary_key=True) #主键
    adminname=models.CharField(max_length=32)
    adminpassword=models.CharField(max_length=32)
    adminsex=models.CharField(max_length=32)



#系统公告
class Announcement(models.Model):
    pass

#管理员表
# class Admin(models.Model):
#     pass