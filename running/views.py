from rest_framework import generics
from .serializers import RunningSerializer
from .models import Running
from .serializers import UsersSerializer
from .models import Users


class RunningList(generics.ListCreateAPIView):
    queryset = Running.objects.all()
    serializer_class = RunningSerializer


class RunningDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Running.objects.all()
    serializer_class = RunningSerializer

class UsersList(generics.ListCreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer


class UsersDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
