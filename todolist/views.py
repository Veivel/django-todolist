
import datetime
from django.shortcuts import render
from todolist.models import Task
from django.contrib.auth import forms
from django.forms import Form

# authentication-related
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# cookie-related
from django.http import HttpResponseRedirect
from django.urls import reverse


@login_required(login_url='login/')
def show_todolist(request):
    ''' A view displaying the user's todo list.'''
    current_username = request.COOKIES['username']
    context = {
        'title':"Here is your todolist.",
        'name': current_username,
        'list_tasks': Task.objects.filter(user=current_username),
        'last_login': request.COOKIES['last_login']
    }
    return render(request, 'todolist.html', context)

@login_required(login_url='login/')
def add_task(request):
    ''' A view serving a form (to the user) to create a new todolist task. '''
    if request.method == "POST":
        form = Form(request.POST)
        
        new_task = Task()
        new_task.user = request.COOKIES['username']
        new_task.date = datetime.date.today()
        new_task.task_name = form.data['task_name']
        new_task.description = form.data['description']
        new_task.save()
        
        response = HttpResponseRedirect(reverse("todolist:show_todolist"))
        messages.success(request, 'Task... saved?')
        return(response)
    else:
        context = {}
        return render(request, 'add_task.html', context)
    
def __flush_tasks():
    ''' In case I need to delete the entire tasks table. '''
    Task.objects.all().delete()

def register(request):
    form = forms.UserCreationForm()

    if request.method == "POST":
        form = forms.UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login_user')
    
    context = {'form':form}
    return render(request, 'register.html', context)
    
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # menyimpan cookies ke response
            response.set_cookie('username', user.get_username())
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)
    
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login_user'))
    response.delete_cookie('last_login')
    return response


