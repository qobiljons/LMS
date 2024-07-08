from django import forms
from django.forms.widgets import SelectDateWidget
from .models import Notes, Tasks
import datetime


class NoteForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = [ 'title', 'content']

class TaskForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = [ 'subject', 'title', 'description', 'due', 'status']
    
    due= forms.DateField(
        widget=SelectDateWidget(attrs={'class': 'form-control'})
    )


class SearchForm(forms.Form):
    search_query = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter search query'}))