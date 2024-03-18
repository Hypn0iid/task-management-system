from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('login', views.login_user, name="login"),
    path('logout', views.logout_user, name="logout"),
    path('register', views.register_user, name="register"),
    path('create_task', views.create_task, name="create_task"),
    path('get_task_details/<int:task_id>', views.get_task_details, name="get_task_details"),
    path('delete_task/<int:task_id>', views.delete_task, name="delete_task"),
    path('edit_task/<int:task_id>', views.edit_task, name="edit_task"),
    path('toggle_task_completion/<int:task_id>', views.toggle_task_completion, name="toggle_task_completion"),
]