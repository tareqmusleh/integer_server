# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.contrib import admin
from .views import NthNumberSequenceView, FirstNNumbersView 

urlpatterns = patterns('',
	url(r'^(?P<sequence>\w+)/first/(?P<n>\d+)/', FirstNNumbersView.as_view(), name='n_terms'),
    url(r'^(?P<sequence>\w+)/(?P<n>\d+)/', NthNumberSequenceView.as_view(), name='nth_term'),
)
