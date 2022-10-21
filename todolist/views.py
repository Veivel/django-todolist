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

# for json view
from django.core import serializers
from django.http import HttpResponse

@login_required(login_url='login/')
def show_todolist(request):
    ''' A view displaying the user's todo list.'''
    
    current_user = request.user
    context = {
        'name': current_user,
        'list_tasks': Task.objects.filter(user=current_user),
        'last_login': request.COOKIES['last_login']
    }
    return render(request, 'todolist.html', context)

@login_required(login_url='login/')
def add_task(request):
    ''' A view serving a form (to the user) to create a new todolist task. '''
    
    if request.method == "POST":
        form = Form(request.POST)
        
        new_task = Task()
        new_task.user = request.user
        new_task.date = datetime.date.today()
        new_task.task_name = form.data['task_name']
        new_task.description = form.data['description']
        new_task.save()
        
        response = HttpResponseRedirect(reverse("todolist:show_todolist"))
        messages.success(request, 'Task saved.')
        return(response)
    else:
        context = {}
        return render(request, 'add_task.html', context)

@login_required(login_url='login/')
def finish_task(request, id):
    ''' Change is_finished status (completion) of a task to True.'''
    
    task = Task.objects.get(pk=id)
    task.is_finished = True
    task.save()
    messages.success(request, "Task complete!")
    
    return redirect("todolist:show_todolist")

@login_required(login_url='login/')
def delete_task(request, id):
    ''' Remove task from database completely.'''
    
    Task.objects.filter(pk=id).delete()
    messages.success(request, "Task successfully deleted.")
    
    return redirect("todolist:show_todolist")

@login_required(login_url='login/')
def delete_all(request):
    ''' Delete (all of) one user's tasks.'''
    
    Task.objects.filter(user=request.user).delete()
    messages.success(request, "Tasks successfully deleted.")
    
    return redirect("todolist:ajax_show_todolist")

def __flush_tasks():
    ''' In case I need to delete the entire tasks table. '''
    
    Task.objects.all().delete()
    messages.success("Flush successful.")
    print("\nFlush successful.\n")
    
# ----- Login/logout/register -----

def register(request):
    form = forms.UserCreationForm()

    if request.method == "POST":
        form = forms.UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login_user')
        else:
            messages.error(request, 'Akun tidak bisa didaftarkan. Periksa kembali data anda.')
            return redirect('todolist:register')
    else:
        context = {'form':form}
        return render(request, 'register.html', context)
    
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("todolist:ajax_show_todolist")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # menyimpan cookies ke response
            response.set_cookie('user', user)
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
            # return response
        
    context = {}
    return render(request, 'login.html', context)
    
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login_user'))
    response.delete_cookie('last_login')
    return response


# ----- Tugas 6 -----

@login_required(login_url='login/')
def get_json(request):
    current_user = request.user
    data = Task.objects.filter(user=current_user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@login_required(login_url='login/')
def ajax_show_todolist(request):
    context = {
        'user': request.user,
        'is_empty': len(Task.objects.filter(user=request.user)) == 0
    }
    print(len(Task.objects.filter(user=request.user)))
    return render(request, 'todolist_ajax.html', context)

#@login_required(login_url='login/')
def add(request):
    ''' Returns the new task in JSON form. '''
    
    if request.method == "POST":
        form = Form(request.POST)
        
        new_task = Task()
        new_task.user = request.user
        new_task.date = datetime.date.today()
        new_task.task_name = form.data['task_name']
        new_task.description = form.data['description']
        new_task.save()
        
        return HttpResponse(serializers.serialize("json",[new_task]), content_type="application/json")