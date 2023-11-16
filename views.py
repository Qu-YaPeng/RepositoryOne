from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
def hello(request):
    return JsonResponse({'django':'it is ok'})
from django.http import JsonResponse


def get_user(request):
    if request.method == 'GET':
        usid = request.GET.get('usid','')
        if usid=='':
            return JsonResponse({'code':100101,'msg':'用户id不能为空'})
        if usid=='1':
            return JsonResponse({'code':100200,'msg':'查询成功','data':{'usid':1,'name':'james','age':36}})
        else:
            return JsonResponse({'code':100102,'msg':'未查询到用户数据'})

    else:
        return JsonResponse({'code': 100103, 'msg': '请求方法错误'})
