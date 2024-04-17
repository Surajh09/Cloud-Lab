
from cgitb import handler
from logging import Handler
from django.contrib import admin
from django.urls import path
from core.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view),
    path('bubble/', bubble_view),
    path('list/', list_view),
    path('merge/', merge_view),
    path('insertion/', insertion_view),
    path('assesment/', assesment_view),
    path('array/', array_view),
    path('login/', login_view),
    path('about/', aboutUs_view),
    path('linkedlist/', linkedlist_view),
    path('stack/', stack_view),
]
handler505 = 'core.views.error_view'
# handler404 = 'core.views.error_view'
