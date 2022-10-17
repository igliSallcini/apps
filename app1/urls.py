from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='Homepage'),
    path('view/<int:apps_id>', views.view_apps, name='view_apps'),
    # path('form', views.todo_form, name='show-form'),
    # path('todo/save', views.save_todo, name='save-todo'),    
    # path('create/', views.create_todo, name='create-todo')
    path('create/', views.TodoView.as_view(), name='create-todo')
]
