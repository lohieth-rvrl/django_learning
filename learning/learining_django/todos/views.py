from django.shortcuts import render, get_object_or_404
from . import models, forms
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

def home(request):
    query = request.GET.get('search', '')
    status_filter = request.GET.get('status', '')
    priority_filter = request.GET.get('priority', '')

    todos = models.todos.objects.all()

    if query:
        todos = todos.filter(title__icontains=query) | todos.filter(description__icontains=query)
    if status_filter:
        todos = todos.filter(status=status_filter)
    if priority_filter:
        todos = todos.filter(priority=priority_filter)

    form = forms.addForm()
    return render(request, 'todos.html', {
        'todos': todos,
        'form': form,
        'query': query,
        'status_filter': status_filter,
        'priority_filter': priority_filter,
    })


@csrf_exempt
@require_POST
def createTodo(request):
    form = forms.addForm(request.POST, request.FILES)
    if form.is_valid():
        todo = form.save(commit=False)
        todo.user = request.user if request.user.is_authenticated else None
        todo.save()
        return JsonResponse({
            'status': 'success',
            'id': todo.id,
            'title': todo.title,
            'description': todo.description,
            'status_value': todo.status,
        })
    return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)

@csrf_exempt
@require_POST
def deleteTodo(request, id):
    todo = get_object_or_404(models.todos, id=id)
    todo.delete()
    return JsonResponse({'status': 'success', 'message': 'Todo deleted successfully'})

@csrf_exempt
@require_POST
def editTodo(request, id):
    todo = get_object_or_404(models.todos, id=id)
    form = forms.addForm(request.POST, instance=todo)
    if form.is_valid():
        form.save()
        return JsonResponse({
            'status': 'success',
            'message': 'Todo updated successfully',
            'title': todo.title,
            'description': todo.description,
            'status_value': todo.status
        })
    return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)

@csrf_exempt
@require_POST
def mark_completed(request, id):
    todo = get_object_or_404(models.todos, id=id)
    todo.status = 'Completed'
    todo.save()
    return JsonResponse({'status': 'success', 'message': 'Todo marked as completed'})