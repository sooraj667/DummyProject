from django.db import models


class Rider(models.Model):
    name=models.CharField(max_length=200)
    age=models.PositiveIntegerField()
    bikemodel=models.PositiveIntegerField()

    class Meta:
        ordering = ["name"]
    
    def __str__(self):
        return self.name
