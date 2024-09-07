



# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('salesforce/login/', views.salesforce_login, name='salesforce_login'),
    path('salesforce/callback/', views.salesforce_callback, name='salesforce_callback'),
    path('salesforce/query/', views.salesforce_query, name='salesforce_query'),
]
