from django import forms
from my_lista.models import Note

class NoteForm(forms.ModelForm):

    class Meta:
        model = Note
        fields = ['title', 'body']

class SearchForm(forms.Form):
    search_word = forms.CharField(label="Search", max_length=100)