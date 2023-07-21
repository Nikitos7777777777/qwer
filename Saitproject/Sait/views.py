
from django.shortcuts import render,redirect, get_object_or_404
from .models import *
from django.http import Http404
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from .forms import carform



def create_view(request):

    if request.method == 'POST':
        form = carform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('initialSite.html')
    else:
        form = carform()
        context = {
            'form' : form
        }
        return render(request, 'Sait/create.html',context)

def car_view(request):
    dataset = car.objects.all()
    return render(request,'Sait/listview.html',{'dataset' : dataset})

def car_detil_view(request,id):
    try:
        data = car.objects.get(id=id)
    except carform.DoesNotExist:
        raise Http404('Такого не существует')

    return render(request,'Sait/detailview.html',{'data' : data})


def update_view(request,id):
    try:
        old_data = get_object_or_404(car,id=id)
    except Exception:
        raise Http404('Такого не существует')

    if request.method == 'POST':
        form = car(request.POST,instance=old_data)
        if form.is_valid():
            form.save()
            return redirect(f'/{id}')
    else:
        form = carform(instance = old_data)
        context = {
            'form':form
        }
        return render(request,'Sait/update.html',context)


def delete_view(request,id):
    try:
        data = get_object_or_404(car,id=id)
    except Exception:
        raise Http404('Такого не сущкствует')

    if request.method == 'POST':
        data.delete()
        return redirect('/')
    else:
        return render(request,'Sait/delete.html')

def home(request):
    return render(request,"Sait/home.html")

class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

def initialSite(request):
    cars = car.objects.order_by('id')
    context = {'cars':cars}
    return render(request, 'Sait/initialSite.html',context)
def Honda(request):
    Opisaniee = Opisanie.objects.order_by('id')
    context = {'Opisaniee':Opisaniee}
    return render(request, 'Sait/Honda.html',context)
def Moskvich(request):
    Modelcars = Modelcar.objects.order_by('id')
    context = {'Modelcars':Modelcars}
    return render(request, 'Sait/Moskvich.html',context)
def Nisann(request):
    Complectacions = Complectacion.objects.order_by('id')
    context = {'Complectacions':Complectacions}
    return render(request, 'Sait/Nisann.html',context)
def Toyta(request):
    Eniges = Enige.objects.order_by('id')
    context = {'Eniges':Eniges}   
    return render(request, 'Sait/Toyta.html',context)
