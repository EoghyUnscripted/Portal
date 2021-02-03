from django.db import models
from django.contrib.auth.models import User
from datetime import date

class ToDoList(models.Model):
    ToDo_Author = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    ToDo_Title = models.CharField(max_length=255)
    ToDo_Date = models.DateField(null=True, blank=True)
    ToDo_Time = models.TimeField(null=True, blank=True, default='00:00')
    ToDo_Location = models.CharField(max_length=255, null=True, blank=True)
    ToDo_Description = models.TextField(null=True, blank=True)
    ToDo_Completed = models.BooleanField()
    ToDo_Complete_Date = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "To-Do Items"
        ordering = ['ToDo_Date', 'ToDo_Time']

    def __str__(self):
        full_name = self.ToDo_Author.first_name + ' ' + self.ToDo_Author.last_name
        label = self.ToDo_Date.strftime('%b %e %Y') + ' ' + self.ToDo_Title + ' - ' + full_name
        return label

    @property
    def is_past_due(self):
        return date.today() > self.ToDo_Date