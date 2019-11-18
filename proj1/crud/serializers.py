from rest_framework import serializers
from crud.models import Note


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'title', 'description', 'created_date', 'updation_date',)
        model = Note