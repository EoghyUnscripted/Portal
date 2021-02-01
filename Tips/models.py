from django.db import models

class Percentage(models.Model):
    Service_Level = (
        ('Great', 'Great'),
        ('Good', 'Good'),
        ('Average', 'Average'),
        ('Poor', 'Poor'),
        ('Miserable', 'Miserable'),
        ('Never Again', 'Never Again'),
    )

    Tip_Service_Level = models.CharField(max_length=255, choices=Service_Level)
    Tip_Percent = models.DecimalField(max_digits=10, decimal_places=2)
    Tip_Service_Description = models.TextField()

    class Meta:
        verbose_name_plural = "Percentages"
        ordering = ['-Tip_Percent']

    def __str__(self):
        label = 'Service Level' + ' ' + self.Tip_Service_Level
        return label

    def percent(self):
        convert = int(self.Tip_Percent * 100)
        output = str(convert) + '%'
        return output