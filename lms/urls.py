from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='dashboard'),
    path('contacts/', views.contacts, name="contacts"), 
    path('notes/', views.notes, name='notes'), 
    path('notes/create/', views.note_create, name='note_create'),
    path('notes/<int:pk>', views.note_details, name='note_details'),
    path('notes/<int:pk>/delete/', views.note_delete, name='note_delete'),
    path('notes/<int:pk>/edit/', views.note_edit, name='note_edit'),
    path('tasks/', views.tasks, name='tasks'),
    path('tasks/create/', views.task_create, name='task_create'),
    path('tasks/<int:pk>/delete/', views.task_delete, name='task_delete'),
    path('tasks/<int:pk>/edit/', views.task_edit, name='task_edit'),
    path('youtube/', views.youtube, name='youtube'),
    path('books/', views.books, name='books'),
    path('dictionary/', views.dictionary, name='dictionary'),
    path('wikipedia/', views.wikipedia, name="wikipedia"),

]