#序列化器

from rest_framework.serializers import Serializer #这是一个类
#以后写的类 都需要继承Serializer

from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

'''class AdminSerializer(serializers.Serializer):
    adminid=serializers.IntegerField()
    #整形 转给前端 转成字符串也可
    # adminid=serializers.CharField()
    adminname =serializers.CharField()
    adminpassword =serializers.CharField()
    adminsex =serializers.CharField()
'''
#序列化器
from app02.models import Admin,Announcement
class AdminModelSerializer(ModelSerializer):
    class Meta:
        model=Admin
        fields="_all_"

#Admin表序列化
# class AdminModelSerializer(ModelSerializer):
#     pass

#UAnnouncement表序列化
class AnnouncementModelSerializer(ModelSerializer):
    pass
