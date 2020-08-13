from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('',views.HomePage,name = "blog-home"),
    path('CreatePost',views.CreatePost,name="CreatePost"),
    path('Post/<int:pk>',views.ViewPost,name='ViewPost'),
    path('Post/Update/<int:pk>',views.UpdatePost,name="UpdatePost"),
    path('Post/Delete/<int:pk>',views.DeletePost,name="DeletePost"),
    path('Post/<str:username>',views.UserPost,name="UserPost")
]
