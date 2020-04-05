from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url('cases/', views.cases, name='cases'),
    url('case_result/', views.case_result, name='case_result'),
    url('case_form/', views.case_form, name='case_form'),
    url(r'^register/$', views.register, name='register')
]
