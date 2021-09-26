from .views import calendar, add_event, update, remove, all_events
from django.urls import path, include
from django.conf.urls import include, url

app_name = "fullcalendar"
urlpatterns = [
url('^calendar', calendar, name='calendar'),
url('^add_event$', add_event, name='add_event'),
url('^update$', update, name='update'),
url('^remove', remove, name='remove'),
url('^all_events', all_events, name='all_events')
]