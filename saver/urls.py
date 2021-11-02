from django.urls import path
from . import views

urlpatterns = [
    path('data/', views.data, name='data'),
    path('delete_data/<data_id>/', views.delete_data, name='delete-data'),
]