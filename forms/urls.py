from django.urls import path
from .views import (home,delete_user,update_user,addbook,deshboard,admindeshboard,adminusers,delete_book,update_book,logout,main,login_admin,adduser)

urlpatterns = [
    path('',home,name='home'),
    path('addbook',addbook,name="addbook"),
    path('deshboard',deshboard,name="deshboard"),
    path('admindeshboard',admindeshboard,name="admindeshboard"),
    path('adminusers',adminusers,name='adminusers'),
    path('delete_book/<str:id>',delete_book,name="delete_book"),
    path('update_book/<str:id>',update_book,name="update_book"),
    path('logout',logout,name="logout"),
    path('main',main,name="main"),
    path('login_admin',login_admin,name='login_admin'),
    path('adduser',adduser,name="adduser"),
    path('deleteuser<str:id>',delete_user,name="delete_user"),
    path('updateuser/<str:id>',update_user,name="update_user")

]
