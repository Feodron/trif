from django.urls import path, include
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('users', TemplateView.as_view(template_name='user_auth.html'), name='user')
]
