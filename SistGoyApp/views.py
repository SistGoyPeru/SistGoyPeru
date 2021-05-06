from django.shortcuts import render,HttpResponse


# Create your views here.

def home(request):
    return render(request,"SistGoyApp/home.html")

def servicios(request):
    return render(request,"SistGoyApp/servicios.html")

def blog(request):
    return render(request,"SistGoyApp/blog.html")

def contacto(request):
    return render(request,"SistGoyApp/contacto.html")   


