from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, time, timedelta
from django.utils import timezone

class ToDoList(models.Model):
    ToDo_Author = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    ToDo_Title = models.CharField(max_length=255)
    ToDo_Time = models.DateTimeField(default=datetime.now, blank=True, null=True)
    ToDo_Location = models.CharField(max_length=255, null=True, blank=True)
    ToDo_Description = models.TextField(null=True, blank=True)
    ToDo_Completed = models.BooleanField()
    ToDo_Complete_Date = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "To-Do Items"
        ordering = ['ToDo_Time']

    def __str__(self):
        full_name = self.ToDo_Author.first_name + ' ' + self.ToDo_Author.last_name
        label = str(self.ToDo_Time.date()) + ' ' + str(self.ToDo_Time.time()) + ' | ' + full_name + ' | ' + self.ToDo_Title
        return label

    @property
    def is_past_due(self):
        delta = timedelta(hours=8)
        currentTime = timezone.now() - delta
        return currentTime > self.ToDo_Time

    def clean_date(self):
        if self.ToDo_Time is not None:
            label = self.ToDo_Time.date()
            return label
        else:
            return False

    def completed_clean_date(self):
        if self.ToDo_Complete_Date is not None:
            label = self.ToDo_Complete_Date.date()
            return label
        else:
            return False