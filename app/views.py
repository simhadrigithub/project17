from django.shortcuts import render

# Create your views here.
d={'name':'simha','age':21}
def data_render(request):
    return render(request,'data_render.html',context=d)

d1={'a':200,'b':300,'c':50}
def data_render1(request):
    return render(request,'data_render1.html',context=d1)

d2={'a':20,'b':30,'c':50}
def data_render2(request):
    return render(request,'data_render2.html',context=d2)

d3={'name':'simhadri','age':21,'hobbies':['cricket','vollybal']}
def data_render3(request):
    return render(request,'data_render3.html',context=d3)