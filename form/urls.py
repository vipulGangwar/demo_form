
from django.urls import path
from . import views

#from .views import

urlpatterns = [
    path('', views.test_form_collection, name="all"),
    path('login', views.test_user, name="user"),
]
