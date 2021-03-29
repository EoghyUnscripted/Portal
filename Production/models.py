from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    Employee_Profile = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE, related_name='profile')
    Employee_Full_Name = models.CharField(max_length=255, null=True, blank=True, default='first last')
    Employee_Title = models.CharField(max_length=255)
    Manager_Name = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='manager')
    Staff_Access = models.BooleanField()

    class Meta:
        verbose_name_plural = "Profiles"

    def __str__(self):
        label = self.Employee_Full_Name
        user = str(label)
        return user

class BasicMenu(models.Model):
    Item_Name = models.CharField(max_length=255)
    Item_Link = models.TextField()

    class Meta:
        verbose_name_plural = "Employee Menus"
        ordering = ['id']

    def __str__(self):
        return self.Item_Name
        
class ProdList(models.Model):
    Department = models.CharField(max_length=255)
    Title = models.CharField(max_length=255)
    Start_Date = models.DateTimeField()
    End_Date = models.DateTimeField(blank=True, null=True)
    Description = models.TextField()
    Disabled = models.BooleanField(default=False)
    Created_By = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['Department', 'Title']
        verbose_name_plural = "Department Tasks"

    def __str__(self):
        label = (self.Title + ' ' + self.Department)
        return label

class ProdEntry(models.Model):
    Assignment_Title = models.ForeignKey(ProdList, on_delete=models.CASCADE)
    Assignment_Date = models.DateTimeField()
    Assignment_Count = models.IntegerField()
    Assignment_Time = models.IntegerField(help_text='Enter total minutes')
    Assignment_Notes = models.TextField()
    Assignment_Owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['Assignment_Date']
        verbose_name_plural = "Completed Assignments"

    def __str__(self):
        label = (self.Assignment_Date.strftime('%b %e %Y') + self.Assignment_Owner 
                    + self.Assignment_Title +  'Count: ' + str(self.Assignment_Count) 
                    + 'Time: ' + str(self.Assignment_Time))
        return label

    def Assignment_Clean_Date(self):
        return self.Assignment_Date.strftime('%b %e %Y')

    def Assignment_Note_Min(self):
        return self.Assignment_Notes[:100]


