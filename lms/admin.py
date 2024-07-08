from django.contrib import admin
from .models import Notes, Tasks

# Register your models here.


@admin.register(Notes)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'content', 'created_at', 'updated_at')
    search_fields = ['title']


@admin.register(Tasks)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('author', 'subject', 'due', 'status')
    search_fields = ['title', 'subject']
    list_editable = ["status"]



