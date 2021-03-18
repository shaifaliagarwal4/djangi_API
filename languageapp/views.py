from django.shortcuts import render
from .serializers import LanguageSerializer
from .models import Language
from rest_framework import viewsets


class LanguageView(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer

