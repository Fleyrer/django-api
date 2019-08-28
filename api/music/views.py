from rest_framework import generics
from .models import Songs
from .serializers import SongsSerializer
from django.shortcuts import render


class ListSongsView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Songs.objects.all()
    serializer_class = SongsSerializer


def index(request):
    return render(request, 'music/index.html')
