from django.urls import path
from . import views

# patrón de URL
urlpatterns = [
    path('', views.post_list, name='post_list'),
]
