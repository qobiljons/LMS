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
    if request.method == 'POST':
        form = SearchForm(request.POST)
        search_term = request.POST['search']
        videos_search = VideosSearch(search_term, limit=25)
        videos = videos_search.result()['result']
        results = []

        for video in videos:
            video_info = {
                'title': video['title'],
                'published_time': video['publishedTime'],
                'duration': video['duration'],
                'views': video['viewCount']['short'],
                'thumbnails': video['thumbnails'][0]['url'],
                # 'description': video['descriptionSnipped'][0]["text"],
                'channel_link': video['channel']['link'],
                'channel_name': video['channel']['name'],
                'channel_thumbnail': video['channel']['thumbnails'][0]['url'],
                'link':video['link']
            }
            results.append(video_info)
        return render(request, 'youtube/youtube.html', {'form': form, 'videos': results})
    else:
        form = SearchForm()
        videos_search = VideosSearch("subjects", limit=25)
        videos = videos_search.result()['result']
        results = []
    for video in videos:
            video_info = {
                'title': video['title'],
                'published_time': video['publishedTime'],
                'duration': video['duration'],
                'views': video['viewCount']['short'],
                'thumbnails': video['thumbnails'][0]['url'],
                'channel_link': video['channel']['link'],
                'channel_name': video['channel']['name'],
                'channel_thumbnail': video['channel']['thumbnails'][0]['url'],
                'link':video['link']
            }
            results.append(video_info)
    return render(request, 'youtube/youtube.html', {'form': form, 'videos': results})