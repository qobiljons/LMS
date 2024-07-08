from django.db import models
from django.conf import settings

# Create your models here.


class Notes(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Note"
        verbose_name_plural = "Notes"


class Tasks(models.Model):
    STATUS = [
        ('F', "Finished"),
        ('U', "Unfinished"),
    ]
    class Meta:
        verbose_name = "Task"
        verbose_name_plural = "Tasks"
        ordering = ["subject", "due"]
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    subject = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    due = models.DateTimeField()
    status = models.CharField(max_length=1, choices=STATUS, default="U")

    def __str__(self):
        return self.title