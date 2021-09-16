from django.urls import path
from . import views
from .views import calendar, add_event, update, remove, all_events 

urlpatterns = [
    path('create/', views.create, name='create'),
    path('^calendar', calendar, name='calendar'),
    path('^add_event$', add_event, name='add_event'),
    path('^update$', update, name='update'),
    path('^remove', remove, name='remove'),
    path('^all_events', all_events, name='all_events'),
]