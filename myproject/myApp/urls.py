from django.urls import path
from myApp import views

urlpatterns = [
    path('',views.home,name='home'),
    path('add',views.addData,name="add"),
    path('update/<id>',views.updateData,name="update"),
    path('delete/<id>',views.deleteData,name="delete")
]