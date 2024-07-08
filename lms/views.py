from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, ListView, DetailView, CreateView, DeleteView
from .models import Notes, Tasks
from .forms import NoteForm, TaskForm, SearchForm
from django.urls import reverse_lazy, reverse
from youtubesearchpython import VideosSearch

# Create your views here.



#Dashboard

class HomePageView(TemplateView):
    template_name = 'index.html'


#Notes App Views

def notes(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.author = request.user
            note.save()
            form = NoteForm()
    else:
        form = NoteForm()
    notes = Notes.objects.filter(author=request.user).order_by('-created_at')
    context = {'notes': notes, 'form': form}
    return render(request, 'notes.html', context=context)

def note_details(request, pk):
    note = get_object_or_404(Notes, pk=pk)
    context = {'note': note}
    return render(request, 'note_details.html', context=context)


def note_delete(request, pk):
    note = get_object_or_404(Notes, pk=pk)
    note.delete()
    return redirect(reverse('notes'))

def note_edit(request, pk):
    note = get_object_or_404(Notes, pk=pk)
    form = NoteForm(instance=note)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect(reverse('note_details', args=[pk]))
    context = {'form': form}
    return render(request, 'note_edit.html', context=context)


def tasks(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.author = request.user
            task.save()
            form = TaskForm()
    else:
        form = TaskForm()
    tasks = Tasks.objects.filter(author=request.user).order_by('-id')
    context = {'tasks': tasks, 'form': form}
    return render(request, 'tasks/tasks.html', context=context)


def task_delete(request, pk):
    task = get_object_or_404(Tasks, pk=pk)
    task.delete()
    return redirect(reverse('tasks'))

def youtube(request):
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            search_query = form.cleaned_data["search_query"]
            video = VideosSearch(search_query, limit=10) 
            print(video.result())  # print the video results in the console
            results = []
            for video_result in video.result()["videos"]:
                results.append(video_result)
            print(results)
            context = {
                "results": results,
                "search_query": search_query,
            }
    form = SearchForm()
    context = {
        "form": form,
    }
    return render(request, 'youtube/youtube.html', context)