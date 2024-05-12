from django.urls import path

from todos import views

urlpatterns = [

    path('', views.dash, name='dash'),
    path('addtask', views.addtask, name='addtask'),
    path('viewtask', views.viewtask, name='viewtask'),
    path('taskupdate/<int:id>/', views.taskupdate, name='taskupdate'),
    path('taskdelete/<int:id>/', views.taskdelete, name='taskdelete'),

]