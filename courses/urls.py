from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.course_list, name= 'list'),


    url(r'(?P<course_pk>\d+)/(?P<step_pk>\d+)/$', views.step_detail,
        name='step'),
    #name of the group, one or more digits that comes to the url
    url(r'(?P<pk>\d+)/$', views.course_detail,
    name='detail'),
]
