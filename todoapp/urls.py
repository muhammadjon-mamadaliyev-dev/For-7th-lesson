from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='home'),
    path('create/',views.create_todo,name='todo_create'),
    path('todos/<int:pk>',views.todo_item,name='todo_item'),
    path('delete/<int:pk>',views.delete,name = 'delete'),
    path('edit/<int:pk>',views.edit,name = 'edit')
]