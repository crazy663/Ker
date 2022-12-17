from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema
from rest_framework.views import APIView
from bs4 import BeautifulSoup
import FuncApp
from .models import Cont
from .serializers import ContSerializer
from FuncApp.func import get_content
import json
import requests


class ContView(APIView):

    @extend_schema(request=ContSerializer, responses=ContSerializer)
    def get(self, request, urlpath):
        content = Cont(urlpath, FuncApp.func.get_content(urlpath))

        serializer_for_request = ContSerializer(instance=content)

        return Response(serializer_for_request.data)


