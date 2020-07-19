from django.urls import path
from .views import index,show
app_name='blog'
urlpatterns=[
    path('', index, name='index'),
    path('<int:article_id>/', show, name='show'),
]