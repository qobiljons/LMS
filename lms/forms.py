from django import forms
from django.forms.widgets import SelectDateWidget
from .models import Notes, Tasks
import datetime


class NoteForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = [ 'title', 'content']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control form-control-sm', 'rows': 7}),
        }

class TaskForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ['subject', 'title', 'description', 'due', 'status']
        widgets = {
            'description': forms.Textarea(attrs={'class': 'form-control form-control-sm', 'rows': 2}),
            'due': SelectDateWidget(attrs={'class': 'form-control', 'style': 'width: auto; padding: 0.2rem; font-size: 0.7rem;display:flex; flex-direction:column;'})
        }


class SearchForm(forms.Form):
    search_query = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter search query'}))