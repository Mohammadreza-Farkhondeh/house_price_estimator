from django.urls import path
from . import views
urlpatterns = [
    path('estimate/', views.EstimateView.as_view(), name='estimate')
]