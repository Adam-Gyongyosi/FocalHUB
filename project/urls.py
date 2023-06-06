"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth.views import LogoutView, LoginView
from django.conf.urls.static import static
from django.conf import settings

from project import views, settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('FocalHUB.urls')),
    path('', include('FocalHUB.urls')),
    path('register/', views.signup, name="reg-page"),
    path('logout/', LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL}, name="logout-page"),
    path('login/', LoginView.as_view(template_name= "login.html"), name="login-page"),
    path('upload/', views.upload_post, name='upload_post'),
    path('feed/', views.feed, name='feed'),
    path('like/<int:post_id>/', views.like_post, name='like_post'),
    path('trending/',views.trending, name='trending'),
    path('usersettings/', views.usersettings, name='usersettings'),
    path('deletepicture/<int:post_id>/', views.deletepicture, name='deletepicture'),
    path('writecomment/<int:post_id>/', views.writecomment, name='writecomment'),
    path('deletecomment/<int:comment_id>/',views.deletecomment, name='deletecomment'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)