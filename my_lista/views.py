from django.shortcuts import render, redirect
from my_lista.models import Note
from my_lista.forms import NoteForm



# Create your views here.
def notes_list(request):
    allnotes = Note.objects.all()
    return render(request, "notes/notes_list.html", {
        "notes": allnotes,
    })
    

def notes_detail(request, pk):
    note = Note.objects.get(pk=pk)
    return render(request, "notes/notes_detail.html",
                  {"note": note})   
                  
def create_note(request):
    
    if request.method == "POST":  # form was submitted
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save()
            return redirect(to='notes_list')
    else:
        form = NoteForm()

    return render(request, "notes/create_note.html", {"form": form})    
