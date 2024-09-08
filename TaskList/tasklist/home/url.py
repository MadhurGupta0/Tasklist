from django.urls import path
from .views import home,add_task,edit_task,delete_task,detail_task,item
urlpatterns = [
    path('', home, name='home'),
    path('add/', add_task, name='add'),
    path('edit/<int:task_id>/', edit_task, name='edit'),
    path('delete/<int:task_id>/', delete_task, name='delete'),
    path('detail/<int:task_id>/', detail_task, name='detail'),
    path('item/', item, name='items'),

]