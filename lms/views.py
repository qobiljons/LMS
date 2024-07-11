import random
import requests
import wikipedia as wiki
from youtubesearchpython import VideosSearch
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, ListView, DetailView, CreateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required
from .models import Notes, Tasks
from .forms import NoteForm, TaskForm, SearchForm, ContactForm

# Create your views here.

#Dashboard


class HomePageView(TemplateView):
    template_name = 'index.html'


#Notes App Views

@login_required
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
    return render(request, 'notes/notes.html', context=context)

@login_required
def note_create(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.author = request.user
            note.save()
            return redirect(reverse('notes'))
    else:
        form = NoteForm()
    context = {'form': form}
    return render(request, 'notes/note_create.html', context=context)

@login_required
def note_details(request, pk):
    note = get_object_or_404(Notes, pk=pk)
    context = {'note': note}
    return render(request, 'notes/note_details.html', context=context)

@login_required
def note_delete(request, pk):
    note = get_object_or_404(Notes, pk=pk)
    note.delete()
    return redirect(reverse('notes'))

@login_required
def note_edit(request, pk):
    note = get_object_or_404(Notes, pk=pk)
    form = NoteForm(instance=note)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect(reverse('note_details', args=[pk]))
    context = {'form': form}
    return render(request, 'notes/note_edit.html', context=context)

@login_required
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

@login_required
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.author = request.user
            form.save()
            return redirect(reverse('tasks'))
    else:
        form = TaskForm()
    return render(request, 'tasks/task_create.html', {'form': form})

@login_required
def task_edit(request, pk):
    task = get_object_or_404(Tasks, pk=pk)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect(reverse('tasks'))
    context = {'form': form}
    return render(request, 'tasks/task_edit.html', context=context)

@login_required
def task_delete(request, pk):
    task = get_object_or_404(Tasks, pk=pk)
    task.delete()
    return redirect(reverse('tasks'))


def youtube(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        search_term = request.POST['search']
        videos_search = VideosSearch(search_term, limit=random.randint(8,13))
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
        videos_search = VideosSearch(get_random_search(), limit=25)
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

def books(request):
    api = "https://www.googleapis.com/books/v1/volumes?q="
    if request.method == 'POST':
        form = SearchForm(request.POST)
        search_term = request.POST['search']
        books_search = api + search_term
        books_data = requests.get(books_search)
        if books_data.status_code == 200:
            try:
                books = books_data.json()['items']
                results = []
                for book in books:
                    book_info = {
                        'title': book['volumeInfo'].get('title'),
                        'authors': book['volumeInfo'].get('authors'),
                        'published_date': book['volumeInfo'].get('publishedDate'),
                        'description': book['volumeInfo'].get('description'),
                        'image_link': book['volumeInfo'].get('imageLinks'),
                        'preview_link': book['volumeInfo'].get('previewLink')
                    }
                    results.append(book_info)
                    print(results)
                return render(request, 'books/books.html', {"form": form, "books":results})
            except KeyError:
                return HttpResponse("Invalid response from Google Books API.")
        else:
            return HttpResponse("Error fetching data from Google Books API.")
    else:
        form = SearchForm()
        books_search = api + get_random_search()
        books_data = requests.get(books_search)
        if books_data.status_code == 200:
            try:
                books = books_data.json()['items']
                results = []
                for book in books:
                    book_info = {
                        'title': book['volumeInfo'].get('title'),
                        'authors': book['volumeInfo'].get('authors'),
                        'published_date': book['volumeInfo'].get('publishedDate'),
                        'description': book['volumeInfo'].get('description'),
                        'image_link': book['volumeInfo'].get('imageLinks'),
                        'preview_link': book['volumeInfo'].get('previewLink')
                    }
                    results.append(book_info)
                    print(results)
                return render(request, 'books/books.html', {"form": form, "books":results})
            except KeyError:
                return HttpResponse("Invalid response from Google Books API.")
        else:
            return HttpResponse("Error fetching data from Google Books API.")

def dictionary(request):
    api = "https://api.dictionaryapi.dev/api/v2/entries/en/"
    if request.method == "POST":
        form = SearchForm(request.POST)
        search_term = request.POST['search']
        dictionary_search = api + search_term
        dictionary_data = requests.get(dictionary_search)
        
        if dictionary_data.status_code == 200:
            word = dictionary_data.json()[0]
            print(word)
            result = {
                    "word": word["word"],
                    "phonetic": word["phonetic"],
                    "audio": word["phonetics"][0]["audio"],
                    "definition": word["meanings"][0]["definitions"][0]["definition"],
                    "synonyms": word["meanings"][0]["definitions"][0]["synonyms"],
                    "antonyms":  word["meanings"][0]["definitions"][0]["antonyms"]
                }
            
            print(result)
            return render(request, 'dictionary/dictionary.html', {'form': form, 'word': result})
            
    form = SearchForm()
    return render(request, 'dictionary/dictionary.html', {'form': form})


def wikipedia(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        search_term = request.POST.get('search', '')
        try:
            page = wiki.page(search_term)
            context = {
                'form': form,
                'title': page.title,
                'content': page.content[:1000] + '...' if len(page.content) > 2000 else page.content,
                'url': page.url,
                'image': page.images[0] if page.images else None,
            }
            return render(request, "wikipedia/wikipedia.html", context=context)
        except Exception as e:
            print(f"An error occurred: {e}")
    
        return render(request, "wikipedia/wikipedia.html", context=None)

    form  = SearchForm()
    return render(request, "wikipedia/wikipedia.html", {"form":form})



def get_random_search():
    random_keywords = ['music', 'technology', 'cooking', 'gaming', 'travel', 'all', 'art', 'song', 'cars', 'learning']
    return random.choice(random_keywords)   



def contacts(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            send_email(name = form.cleaned_data["name"], email=form.cleaned_data["email"], message=form.cleaned_data["message"] )
        else:
            return HttpResponse("Invalid Form!")
    form = ContactForm()
    return render(request, "contacts.html", context={"form":form})
 

def send_email(name, email, message):
    print(f"Sending {message} to {name} with {email}")


