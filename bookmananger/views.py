from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse

# Create your views here.
"""
视图
所谓视图，就是一个python函数
这个函数要求有两个要求
要求一：接收请求
要求二：必须要返回数据
"""


def index(request):
    context ={
        'name': 'tyt',
        'age': 18,
        'gender': '女'
    }
    return render(request, 'index.html', context=context)