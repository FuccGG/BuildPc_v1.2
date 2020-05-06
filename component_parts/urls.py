from django.conf.urls import url
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url('cases/', views.cases, name='cases'),
    url('case_result/', views.case_result, name='case_result'),
    url('case_form/', views.case_form, name='case_form'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', LogoutView, {'template_name': 'accounts/logout.html'}, name='logout'),
    url(r'^register/$', views.register, name='register')
]
