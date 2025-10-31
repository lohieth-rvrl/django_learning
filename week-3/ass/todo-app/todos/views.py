from django.shortcuts import render, redirect, get_object_or_404
from . import models
from . import forms
from django.contrib import messages

def home(request):
    todos = models.todos.objects.all()
    return render(request, 'home.html', {'todos': todos})


def createTodo(request):
    if request.method == 'POST':
        form = forms.addForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Todo created successfully')
            return redirect('home')
    else:
        form = forms.addForm()
    return render(request, 'create.html', {'form': form})

def deleteTodo(request, id):
    todo = get_object_or_404(models.todos, id=id)
    if request.method == 'POST':
        todo.delete()
        messages.success(request, 'Todo deleted successfully')
        return redirect('home')
    return render(request, 'delete.html', {'todo': todo})

def editTodo(request, id):
    todo = get_object_or_404(models.todos, id=id)
    if request.method == 'POST':
        form = forms.addForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            messages.success(request, 'Todo edited successfully')
            return redirect('home')
    else:
        form = forms.addForm(instance=todo)
    return render(request, 'create.html', {'form': form})

def mark_completed(request, id):
    todo = get_object_or_404(models.todos, id=id)
    todo.status = 'Completed'
    messages.success(request, 'Todo marked as completed')
    todo.save()
    return redirect('home')
