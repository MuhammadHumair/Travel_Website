from django.urls import path
from userpanel import views
from account import views as acc_view

urlpatterns = [
    path('', views.index, name='index'),
    path('account/logout', acc_view.logout, name='index')
]
