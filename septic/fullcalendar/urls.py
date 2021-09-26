from .views import calendar, add_event, update, remove, all_events
from django.urls import path, include

app_name = "fullcalendar"
urlpatterns = [
path('calendar', calendar, name='calendar'),
path('add_event', add_event, name='add_event'),
path('update', update, name='update'),
path('remove', remove, name='remove'),
path('all_events', all_events, name='all_events')
]