from django.shortcuts import render
from rest_framework import generics, viewsets
from crud.models import Note
from crud.serializers import NoteSerializer
#from rest_framework import viewsets
# Create your views here.

#class NoteList(generics.ListAPIView):
 #   queryset = Note.objects.all()
  #  serializer_class = NoteSerializer


#class NoteDetail(generics.RetrieveUpdateAPIView):
 #   queryset = models.Note.objects.all()
  #  serializer_class = serializers.NoteSerializer

class Noteviewset(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


