from django.http import JsonResponse
from django.shortcuts import render,redirect
from django.views.generic import View
from .models import Order,Course
from .forms import OrderForm
from django.contrib import messages
def demo(request):
    return render(request,'index.html')

def home(request):
    return render(request,'order.html')

class Orderview(View):
    def get(self,request,*args,**kwargs):
        form=OrderForm()
        return render(request,'add.html',{'form':form})

    def post(self, request, *args, **kwargs):
        form=OrderForm(request.POST)

        if form.is_valid():
            form.save()
            messages.info(request, 'order confirmed')
            return render(request,"add.html",{'form':form})
        else:
            return render(request,"add.html",{'form':form})

def load_courses(request):
    deptname_id = request.GET.get('deptname_id')
    courses = list(Course.objects.filter(deptname__id=deptname_id).values())
    return JsonResponse({'courses': courses})
