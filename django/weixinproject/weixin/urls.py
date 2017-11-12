from django.conf.urls import url

from . import views

app_name = 'weixin'
urlpatterns = [
    url(r'^weixin/index$', views.index, name='index'),
]
