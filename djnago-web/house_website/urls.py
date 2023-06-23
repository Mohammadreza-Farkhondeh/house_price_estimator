from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('price/', include('price_estimator.urls')),
]
