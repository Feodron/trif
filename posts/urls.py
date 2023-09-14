from django.urls import path
from . import views

urlpatterns = [
    path('', views.posts_home, name='posts_home'),
    path('create', views.create, name='create'),
    path('<int:pk>', views.PostsDetailView.as_view(), name='posts-detail'),
    path('<int:pk>/update', views.PostUpdateView.as_view(), name='posts-update'),
    path('<int:pk>/delete', views.PostDeleteView.as_view(), name='posts-delete')
]
