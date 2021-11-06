from django.shortcuts import render,HttpResponse,redirect
from app02 import models


# Create your views here.
def index(request):
    #业务逻辑


    #返回结果
    #return HttpResponse('INDEX') #返回一个字符串
    return render(request,'index.html')

def login(request):

    # print(request.type(request))
    # print(request.method,type(request.method))

    if  request.method=='POST':
        # print(request.POST,type(request.POST))
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
        # print(user,pwd)
        #if user=="fuqc" and pwd =="123":
        if models.User.objects.filter(username=user,password=pwd):
            # return HttpResponse("chenggong")
            return redirect('/index/')
            # return redirect("http://www.baidu.com")  可以返回地址或者路径 都是可以的

    return render(request,'login.html')


def test(request): #c测试方法

    ret=models.User.objects.all()  #获取表中所哟数据，返回的是一个对象 列表 打印如下
    for i in ret:
        print(i.userid,i.username,i.password,type(i.userid))
    print(ret,type(ret))


    #ret=models.User.objects.get(username='fuqc',password='123') #获取数据 返回对象  ；但获取不到；或者多条数据会报错

    #ret=models.User.objects.filter()  #获取满足条件的对象列表 返回一个对象、空对象、


    return render(request,'test.html')

'''
from rest_framework.views import APIView
from app02.models import Admin
#from app02.ser import AdminSerializer
from rest_framework.response import Response

#管理员类
class AdminView(APIView):
    def get(self,request,pk):
        admin=Admin.objects.filter(adminid=pk).filter()
        #s实例化类
        #序列化谁 把谁传过来
        admin_ser=AdminSerializer(admin)   #调用类的_init_)

        return Response(admin_ser.data)   #拿到序列化后的字典
'''


from rest_framework.viewsets import ModelViewSet
from .models import Admin
from .ser import AdminModelSerializer


class AdminViewSet(ModelViewSet):
    queryset = Admin.objects.all()
    serializer_class = AdminModelSerializer



# class AdminViewSet(ModelViewSet):
#     #登录
#     def login(self):
#         pass
#
#     #登出
#     def logout(self):
#         pass
#
#     #编辑信息
#     def modify_info(self):
#         pass
#
#     #用户管理
#     def manageUser(self):
#         pass

class AnnouncementViewSet(ModelViewSet):
    #发布通告
    def deliverAnn(self):
        pass

    #删除通告
    def manageAnn(self):
        pass