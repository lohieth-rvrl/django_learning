from django.shortcuts import render

def home(request):
    return render(request, 'src/layouts/master.html', {})

def base(request):
    return render(request, 'base.html', {})

def pro(request, name, age):
    return render(request, 'pro.html', {'name':name, 'age':age})