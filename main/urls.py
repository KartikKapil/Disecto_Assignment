from django.urls import path
from .views import home, getAllItems

urlpatterns = [
    path('',home,name='home'),
    path('getAllItems/',getAllItems,name="Getallitems")
]
