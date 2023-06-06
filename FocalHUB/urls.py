from django.urls import path,include


from FocalHUB import views

urlpatterns = [
    path('', views.home),
]