from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Academic
from .serializers import AcademicSerializer


class AcademicListCreateView(generics.ListCreateAPIView):
    queryset = Academic.objects.all()
    serializer_class = AcademicSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class AcademicDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Academic.objects.all()
    serializer_class = AcademicSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]