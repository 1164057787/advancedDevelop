from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet
from .models import User,Goods,Goods_comments,Category
from app01.models import Trade_info,Trade_state,Goods_comments


class UserViewSet(ModelViewSet):
    #登录
    def login(self):
        pass

    #登出
    def logout(self):
        pass

    #注册
    def register(self):
        pass

    #状态检查
    def check_state(self):
        pass

    def modify_info(self):
        pass


class GoodsViewSet(ModelViewSet):
    #获取商品列表
    def getGoodsList(self):
        pass

    #商品详情
    def getGoodsDetail(self):
        pass

    #商品增加
    def addGoods(self):
        pass

    #商品修改
    def modifyGoods(self):
        pass

    #商品下架
    def deleteGoods(self):
        pass

    #商品状态
    def GoodsState(self):
        pass

    #搜索
    def searchGoods(self):
        pass

    #购物车
    def shoppingCart(self):
        pass



class Goods_commentsViewSet(ModelViewSet):
    #评论增加
    def addComm(self):
        pass



    #评论删除
    def deleteComm(self):
        pass

    #获取评论
    def getComm(self):
        pass


class CategoryViewSet(ModelViewSet):
    #获取商品类别
    def getCategory(self):
        pass

    # 增加商品类别
    def addCategory(self):
        pass

    # 删除商品类别
    def daleteCategory(self):
        pass


class Trade_infoViewSet(ModelViewSet):
    # 获取订单信息
    def getTrade_info(self):
        pass

    #下单
    def addTrade_info(self):
        pass

    # 取消订单
    def cancelTrade_info(self):
        pass

class Trade_stateViewSet(ModelViewSet):
    #订单状态获取
    def getTradeState(self):
        pass



