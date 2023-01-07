from django.urls import path
from .views import *

urlpatterns = [

    path('get/', main_GET),
    path('post/', main_POST),
    path('update/<id>/', main_Update),
    path('delete/<id>/', main_Delete),

]
