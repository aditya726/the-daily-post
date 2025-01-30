from . import views
from django.urls import path
from django.shortcuts import render,redirect
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index,name = 'index'),
    path('signup',views.signup,name = 'signup'),
    path('login',views.login,name = 'login'),
    path('logout',views.logout,name = 'logout'),
    path('blog/<int:id>',views.blog,name = 'blog'),
    path('post',views.post,name = 'post')
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)