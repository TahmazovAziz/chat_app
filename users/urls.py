from django.urls import path, include
from . import views
from django.views.generic import TemplateView
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('do_logout/', views.LogoutView.as_view(), name='logout'),
    path('registr', views.Registr.as_view(), name='registr')

]
