from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_POST, require_GET

from django.views.decorators.csrf import csrf_exempt
from . import models, forms

def home(request):
    data = models.Sheet.objects.filter(user=request.user).order_by('-date')
    form = forms.createform()
    return render(request, 'home.html', {'data': data, 'form': form})

@require_POST
def create(request):
    try:
        form = forms.createform(request.POST, request.FILES)
        if form.is_valid():
            timesheet = form.save(commit=False)
            timesheet.user = request.user
            timesheet.save()
            return JsonResponse({
                'status': 'success',
                'message': 'Timesheet created',
                'id': timesheet.id
            })
        else:
            return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)

@csrf_exempt
def edit(request, id):
    entry = get_object_or_404(models.Sheet, id=id, user=request.user)

    if request.method == 'POST' and request.POST.get('_method') == 'PUT':
        form = forms.createform(request.POST, request.FILES, instance=entry)
        if form.is_valid():
            form.save()
            return JsonResponse({'message': 'Edited successfully'}, status=200)
        return JsonResponse({'errors': form.errors}, status=400)

    return JsonResponse({'error': 'Invalid method'}, status=405)

@csrf_exempt
def delete(request, id):
    if request.method == 'DELETE':
        try:
            entry = models.Sheet.objects.get(id=id, user=request.user)
            entry.delete()
            return JsonResponse({'message': 'Deleted successfully'}, status=200)
        except models.Sheet.DoesNotExist:
            return JsonResponse({'error': 'Not found'}, status=404)

    return JsonResponse({'error': 'Invalid method'}, status=405)


# @require_GET
# def load_modules(request):
#     project_id = request.GET.get('project')
#     modules = models.Module.objects.filter(project_id=project_id).values('id', 'name')
#     return JsonResponse(list(modules), safe=False)

# @require_GET
# def load_tasks(request):
#     module_id = request.GET.get('module')
#     tasks = models.Task.objects.filter(module_id=module_id).values('id', 'name')
#     return JsonResponse(list(tasks), safe=False)
