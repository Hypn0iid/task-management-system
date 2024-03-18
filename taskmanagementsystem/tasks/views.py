from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Task
from .forms import TaskForm, RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.template.loader import render_to_string
from django.urls import reverse

def index(request):
  if request.user.is_authenticated:
    tasks = Task.objects.filter(user=request.user).order_by('-created_at')
    form = TaskForm()

    selected_task = None
    task_id = request.GET.get('task_id')
    if task_id:
      selected_task = get_object_or_404(Task, pk=task_id)

    return render(request, 'index.html', {'tasks': tasks, 'form': form, 'selected_task': selected_task})
  else:
    return redirect('login')

def login_user(request):
  if request.user.is_authenticated:
    return redirect('index')
  else:
    if request.method == "POST":
      username = request.POST['username']
      password = request.POST['password']
      user = authenticate(request, username=username, password=password)
      if user is not None:
        login(request, user)
        messages.success(request, ("Entrou com sucesso!"))
        return redirect('index')
      else:
        messages.error(request, ("Os dados inseridos não estão corretos! Tente novamente"))
        return redirect('login')
    else:
      return render(request, 'login.html')

def logout_user(request):
  if request.user.is_authenticated:
    logout(request)
    messages.success(request, ("Saiu com sucesso!"))

  return redirect('login')

def register_user(request):
  if request.user.is_authenticated:
    return redirect('index')
  else:
    form = RegisterForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
      form.save()

      username = form.cleaned_data['username']
      password = form.cleaned_data['password1']
      user = authenticate(username=username, password=password)

      login(request, user)
      messages.success(request, ("Registou-se com sucesso!"))
      return redirect('index')
    else:
      return render(request, 'register.html', {'form':form})

def create_task(request):
    if request.method == "POST":
      form = TaskForm(request.POST)
      if form.is_valid():
        task = form.save(commit=False)
        task.user = request.user
        task.save()

        tasks = Task.objects.filter(user=request.user).order_by('-created_at')
        tasks_data = [{'id': task.id, 'title': task.title, 'description': task.description, 'due_date': task.due_date, 'priority': task.priority, 'is_completed': task.is_completed} for task in tasks]

        return JsonResponse({'tasks': tasks_data, 'new_task_id': task.id})
      else:
        errors = form.errors.as_json()
        return JsonResponse({'errors': errors}, status=400)
    return JsonResponse({'error': 'Method not allowed'}, status=405)

def get_task_details(request, task_id):
  task = Task.objects.get(pk=task_id)
  if task and request.user == task.user:
    task_details_html = render_to_string('partials/_show_task.html', {'selected_task': task})
    return HttpResponse(task_details_html)
  else:
    return redirect('index')

def delete_task(request, task_id):
  task = Task.objects.get(pk=task_id)
  if task and request.user == task.user:
    task.delete()
    messages.success(request, ("Tarefa eliminada com sucesso!"))
  else:
    messages.error(request, ("Erro!"))
  return redirect('index')

def edit_task(request, task_id):
  task = get_object_or_404(Task, pk=task_id)
  if task and request.user == task.user:
    if request.method == 'POST':
      form = TaskForm(request.POST, instance=task)
      if form.is_valid():
        form.save()
        messages.success(request, 'Tarefa atualizada com sucesso!')
        return HttpResponseRedirect(f"{reverse('index')}?task_id={task.id}")
    else:
      form = TaskForm(instance=task)
    form_url = reverse('edit_task', args=[task_id])
    return render(request, 'edit_task.html', {'form': form, 'form_action': 'Atualizar', 'form_url': form_url, 'task_to_edit': task})
  else:
    messages.error(request, ("Erro!"))
  return redirect('index')

def toggle_task_completion(request, task_id):
  task = get_object_or_404(Task, pk=task_id)
  if task and request.user == task.user:
    if request.method == 'POST':
      task.is_completed = not task.is_completed
      task.save()
      return JsonResponse({'success': True})
  return JsonResponse({'error': 'Erro!'}, status=404)