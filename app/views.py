from django.shortcuts import render

# Create your views here.
d={'name':'simha','age':21}
def data_render(request):
    return render(request,'data_render.html',context=d)

d={'a':20,'b':30,'c':50}
def data_render1(request):
    return render(request,'data_render1.html',context=d)