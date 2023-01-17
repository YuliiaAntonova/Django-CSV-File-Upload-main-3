from django.conf.urls import url
from django.urls import path
from .views import handle
from . import views

app_name = 'csvs'

urlpatterns = [
    path('', handle, name='upload-view'),
    url(r'^about/$', views.aboutview.as_view(), name='upload'),
]
