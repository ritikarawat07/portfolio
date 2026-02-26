from rest_framework import generics
from .models import Achievement
from .serializers import AchievementSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class AchievementListCreateView(generics.ListCreateAPIView):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class AchievementDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]