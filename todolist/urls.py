from django.urls import path
from todolist.views import *

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login_user'),
    path('logout/', logout_user, name='logout_user'),
    path('create-task/', add_task, name='add_task'),
    path('finish-task/<int:id>', finish_task, name='finish_task'),
    path('delete-task/<int:id>', delete_task, name='delete_task'),
    path('delete-all', delete_all, name='delete_all'),
    path('json', get_json, name='get_json'),
    path('ajax', ajax_show_todolist, name='ajax_show_todolist'),
    path('add', add, name='add')
]