from django.urls import path
from .views import AchievementListCreateView, AchievementDetailView

urlpatterns = [
    path('', AchievementListCreateView.as_view(), name='achievement-list-create'),
    path('<int:pk>/', AchievementDetailView.as_view(), name='achievement-detail'),
]