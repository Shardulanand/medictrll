from django.urls import path
from .views import *
app_name='app1'

urlpatterns = [
    path('base/1234',base,name='baseurls'),
    path('base/5678',base,name='baseurls'),
    path('',index,name='indexurls'),
    path('callback/',callback,name='callbackurls'),
    path('about/',about,name='abouturls'),
    path('policy-policy/',policy,name='policyurls'),
]
