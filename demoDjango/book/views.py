from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.



def index(request):
    return render(request, 'index.html', {})

# 后端传入值，再返回值


def test(request):
    n1 = int(request.POST.get('num1'))
    n2 = int(request.POST.get('num2'))

    # 后端数据传给前段
    return HttpResponse(n1+n2)
