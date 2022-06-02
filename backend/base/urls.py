from django.urls import path, include
from . import views

# urls for apis
urlpatterns = [
    # api to see the list of all records.
    path('all/', views.getRecords, name='records'),
    # api to add a new record
    path('new/', views.createRecord, name='add-record'),
]
