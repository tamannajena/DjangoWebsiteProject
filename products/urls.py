from django.urls import path
from . import views

# products/new
urlpatterns = [
    path('',views.index),
    path('new',views.newindex)

]