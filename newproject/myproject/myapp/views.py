from django.shortcuts import render
from .models import *
from .serializers import *
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class ClienttList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        client = Client.objects.all()
        serializer = EventSerializer(snippets, many=True)
        return Response(serializer.data)