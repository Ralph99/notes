from rest_framewor import serializers

from .models import Note

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['author', 'body', 'date']