from django import forms
from my_lista.models import Note

class NoteForm(forms.ModelForm):

    class Meta:
        model = Note
        fields = ['title', 'body']