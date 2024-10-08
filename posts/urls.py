from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.posts_lists,name='list' ),
    path('new-post/', views.new_post,name='new_post' ),
    path('<slug:slug>', views.post_page,name='page' ),
]
