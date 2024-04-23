from django.urls import path
from newsletter import views

urlpatterns = [
    path('newsletter/', views.NewletterListCreateView.as_view()),
    path('newsletter/<int:pk>/', views.NewletterRetrieveUpdateDestroyView.as_view()),
]