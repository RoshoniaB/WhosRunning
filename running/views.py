from rest_framework import generics
from .serializers import RunningSerializer
from .models import Running


class RunningList(generics.ListCreateAPIView):
    queryset = Running.objects.all()
    serializer_class = RunningSerializer


class RunningDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Running.objects.all()
    serializer_class = RunningSerializer
