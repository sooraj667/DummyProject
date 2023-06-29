from django.urls import path,include
from rxapp import views
urlpatterns = [
    path("",views.base)

]