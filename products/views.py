from django.shortcuts import render

# Create your views here.


def product_list(requset):
        return render(requset,'products.html')

def publish(request):
    if request.method == 'GET':
         return render(request,'publish.html')
    elif request.method == 'POST':
         app_name = request.POST['APP名称']
         intro    = request.POST['介绍']
         url      = request.POST['APP链接']
         icon     = request.FILES['APP图标']
         image    = request.FILES['大图']