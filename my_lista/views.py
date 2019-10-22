from django.shortcuts import render
from my_lista.models import Note



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
    
