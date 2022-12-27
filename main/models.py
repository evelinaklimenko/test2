from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    data = models.DateField()
    image = models.ImageField(upload_to='image', null=True, blank=True)

    def __str__(self) -> str:
        return self.title