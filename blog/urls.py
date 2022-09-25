from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post_detail/<int:post_id>', views.post_detail, name='post_detail'),
    path('add_post/', views.add_post, name='add_post'),
    path('delete_post/<int:post_id>', views.delete_post, name='delete_post'),
]