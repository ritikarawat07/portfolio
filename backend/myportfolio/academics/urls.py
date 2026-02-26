from django.urls import path
from .views import AcademicListCreateView, AcademicDetailView

urlpatterns = [
    path('', AcademicListCreateView.as_view(), name='academic-list-create'),
    path('<int:pk>/', AcademicDetailView.as_view(), name='academic-detail'),
]