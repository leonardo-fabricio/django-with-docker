from django.urls import path
from blog.views import *


app_name = 'blog'

urlpatterns = [
    path("/", MyFunction, name='index' ),
]
