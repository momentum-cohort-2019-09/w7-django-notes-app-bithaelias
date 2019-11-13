from django.shortcuts import render, redirect, get_object_or_404
from my_lista.models import Note
from my_lista.forms import NoteForm, SearchForm


def notes_list(request):
    allnotes = Note.objects.all()
    if request.method =="POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            search_word = form.cleaned_data['search_word'].lower()
            allnotes = allnotes.filter(title__icontains=search_word)
    else:
        form = SearchForm()
    return render(request, "notes/notes_list.html", {
        "notes": allnotes,
        "form": form,
    })
    

def notes_detail(request, pk):
    note = Note.objects.get(pk=pk)
    return render(request, "notes/notes_detail.html",
                  {"note": note})   
                  
def create_note(request):
    
    if request.method == "POST":  
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save()

            return redirect(to='notes_list')
    else:
        form = NoteForm()

    return render(request, "notes/create_note.html", {"form": form}) 

def edit_note(request, pk):
    note = get_object_or_404(Note, pk=pk)
    
    if request.method == "POST":
        form = NoteForm(instance=note, data=request.POST)
        if form.is_valid():
            note = form.save()
            return redirect(to='notes_detail', pk=note.pk)
    else:
        form = NoteForm(instance=note)

    return render(request, 'notes/edit_note.html', {
        "note": note,
        "form": form,
    })  
    
def delete_note(request, pk):
    note = get_object_or_404(Note, pk=pk)         
    if request.method == "POST":
        note.delete()
        return redirect(to='notes_list')

    return render(request, 'notes/delete_note.html', {"note":note}) 



    
   

     




