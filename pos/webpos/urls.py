from django.conf.urls import patterns, url
from webpos import views
from django.contrib.auth.decorators import login_required

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^order/$', views.order, name='order'),
    url(r'^refresh/$', views.refresh_buttons, name='refresh'),
    # url(r'^commit/$', views.commit_bill, name='commit'),
    url(r'^report/(\?(\w=[0-9A-Z%]&?)+)?$', login_required(views.report), name='report'),
    url(r'^bill/(?P<pk>\d+)/$', login_required(views.BillDetailView.as_view()),
        name='bill-detail'),
    url(r'^search/(\?search=[0-9a-zA-Z%]*)?$', login_required(views.search), name='search'),


)
