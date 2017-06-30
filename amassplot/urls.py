from django.conf.urls import url

from . import views

# app_name = 'fruits'
urlpatterns = [
    # ex: /amassplot/
    url(r'^$', views.index, name='index'),
]