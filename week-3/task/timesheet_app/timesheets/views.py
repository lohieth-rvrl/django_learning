from django.shortcuts import render, redirect, get_object_or_404
from . import models
from . import forms
from django.contrib import messages

def home(request):
    data = models.Sheet.objects.filter(user = request.user).order_by('-date')
    return render(request, 'home.html', {'data' : data})

def create(request):
    if request.method == 'POST':
        form = forms.createform(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.user = request.user
            entry.save()
            messages.success(request, 'created successful')
            return redirect('home')
    else:
        form = forms.createform()
    return render(request, 'create.html', {'form': form})

# def create(request):
#     if request.method == 'POST':
#         project = request.POST.get('project')
#         module = request.POST.get('module')
#         task = request.POST.get('task')
#         date = request.POST.get('date')
#         time = request.POST.get('time')
#         description = request.POST.get('description')

#         models.Sheet.objects.create(project=project,module=module,task=task,date=date,time=time,description=description)
#         return redirect('home')
#     data = models.Sheet.objects.all()
#     return render(request, 'create.html', {'data': data})

def delete(request, id):
    entry = models.Sheet.objects.get(id=id)
    entry.delete()
    messages.success(request, 'deleted successful')
    return redirect('home')

def edit(request, id):
    entry = get_object_or_404(models.Sheet, id=id, user=request.user)
    if request.method == 'POST':
        form = forms.createform(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            messages.success(request, 'edited successful')
            return redirect('home')
    else:
        form = forms.createform(instance=entry)
    return render(request, 'create.html', {'form': form})
