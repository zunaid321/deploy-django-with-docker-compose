from django.urls import path
from .views import *


urlpatterns = [
    path('services', ServiceListView.as_view()),
    path('service/<int:id>', ServiceDetailView.as_view()),
    path('newsList', NewsListView.as_view()),
    path('news/<int:id>', NewsDetailView.as_view()),
    path('clients', ClientListView.as_view()),
]
