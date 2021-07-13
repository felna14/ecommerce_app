from django.urls import path
from .import views

urlpatterns=[
      path('search',views.searchResult,name='searchResult'),
]