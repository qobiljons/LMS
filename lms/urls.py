from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='dashboard'),
    path('notes/', views.notes, name='notes'), 
    path('notes/<int:pk>', views.note_details, name='note_details'),
    path('notes/<int:pk>/delete/', views.note_delete, name='note_delete'),
    path('notes/<int:pk>/edit/', views.note_edit, name='note_edit'),
    path('tasks/', views.tasks, name='tasks'),
    path('tasks/<int:pk>/delete/', views.task_delete, name='task_delete'),
    path('youtube/', views.youtube, name='youtube'),
    path('books/', views.books, name='books')
]