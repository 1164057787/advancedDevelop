#序列化器
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from app01.models import User,Goods,Goods_comments,Category
from app01.models import Trade_info,Trade_state,Goods_comments


#序列化器
#User表序列化
class UserModelSerializer(ModelSerializer):
    pass

#GoodsModelSerializer表序列化
class GoodsModelSerializer(ModelSerializer):
    pass

#Goods_comments表序列化
class Goods_commentsModelSerializer(ModelSerializer):
    pass

#Category表序列化
class CategoryModelSerializer(ModelSerializer):
    pass

#Trade_info表序列化
class Trade_infoModelSerializer(ModelSerializer):
    pass

#Trade_state表序列化
class Trade_stateModelSerializer(ModelSerializer):
    pass



