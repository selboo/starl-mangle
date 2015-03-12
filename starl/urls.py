#!/usr/bin/env python
#_*_encoding:utf-8_*_
# encoding:utf-8
from django.conf.urls import patterns, include, url
import settings
from starl.views import *
from starl.views_user import *
from starl.views_site import *
from starl.views_assets_server import *
from starl.views_assets_office import *
from switch.views import *
from switch.views_monitor import *
from switch.monitor_crontab import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'starl.views.home', name='home'),
    # url(r'^starl/', include('starl.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$',default),
    url(r'^index/$', index),
    url(r'^reg/$', reg),
    url(r'^login/$', login),
    url(r'^logout/$', logout),
    url(r'^status/$', status),
    url(r'^logoutS/$', logoutS),
    url(r'^logoutC/$', logoutC),
    url(r'^site/$', site),
    url(r'^api/session/([a-zA-Z0-9]{1,100})$', api_session),

    # 用户
    url(r'^user/$', user),
    url(r'^user/add/$', user_add),
    url(r'^user/view/([a-zA-Z0-9]{1,10})$', user_view),
    url(r'^user/edit/(\d{1,10})$', user_edit),
    url(r'^user/delete/(\d{1,10})$', user_delete),

    # 网络设备
    url(r'^switch/$', switch),
    url(r'^switch/add/$', switch_add),
    url(r'^switch/view/(\d{1,10})$', switch_view),
    url(r'^switch/edit/(\d{1,10})$', switch_edit),
    url(r'^switch/delete/(\d{1,10})$', switch_delete),
    url(r'^switch/bonding/$', switch_bonding),
    url(r'^switch/switch_tools/$', switch_tools),

    url(r'^monitor/network/$', monitor_network),
    url(r'^monitor/server/$', monitor_server),
    url(r'^monitor/crontab/$', monitor_tarffic),

    # 设备资产
    url(r'^assets/server/$', assets_server),
    url(r'^assets/server/add/$', assets_server_add),
    url(r'^assets/server/view/(\d{1,10})$', assets_server_view),
    url(r'^assets/server/edit/(\d{1,10})$', assets_server_edit),
    url(r'^assets/server/delete/(\d{1,10})$', assets_server_delete),

    # 办公资产
    url(r'^assets/office/$', assets_office),
    url(r'^assets/office/add/$', assets_office_add),
    url(r'^assets/office/view/(\d{1,10})$', assets_office_view),
    url(r'^assets/office/edit/(\d{1,10})$', assets_office_edit),
    url(r'^assets/office/delete/(\d{1,10})$', assets_office_delete),

    # template
    url(r'^css/(?P<path>.*)$', 'django.views.static.serve', {'document_root': "/root/starl/template/css", 'show_indexes': True}),
    url(r'^js/(?P<path>.*)$', 'django.views.static.serve', {'document_root': "/root/starl/template/js", 'show_indexes': True}),
    url(r'^img/(?P<path>.*)$', 'django.views.static.serve', {'document_root': "/root/starl/template/img", 'show_indexes': True}),
    url(r'^switch/(?P<path>.*)$', 'django.views.static.serve', {'document_root': "/root/starl/template/img/switch", 'show_indexes': True}),

    # text
    url(r'^hello/$', hello),
    url(r'^time/(get)/(\d{1,2})/$',current_time),
    url(r'^index_temp/([a-z]{1,10})$',index_temp),
    url(r'^index_temp_color/([a-z]{1,10})/(\d{1,6})$',index_temp_color),
    url(r'^index_temp_file/(\d{1,6})/([a-zA-z0-9]{1,6})$',index_temp_file),
)
