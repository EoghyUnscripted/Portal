from django.db import models

class Demo(models.Model):
    Demo_Name = models.CharField(max_length=255)
    Demo_Image = models.ImageField(upload_to='images/')
    Demo_Version = models.CharField(max_length=5)
    Demo_Description = models.TextField()
    Demo_Date_Developed = models.DateField(null=True, blank=True)
    Demo_Update_Date = models.DateTimeField(null=True, blank=True)
    Demo_Link = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Demos"
        ordering = ['Demo_Name']

    def __str__(self):
        return self.Demo_Name

    def summary(self):
        return self.Demo_Description[:200]        