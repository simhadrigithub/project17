from django.shortcuts import render

# Create your views here.
d={'name':'simha','age':21}
def data_render(request):
    return render(request,'data_render.html',context=d)