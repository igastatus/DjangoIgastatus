from django.urls import path
from igastatus import views

urlpatterns = [
    path('', views.igastatus, name='igastatus'),
]
