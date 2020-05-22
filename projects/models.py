from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=50)
    header = models.CharField(max_length=100)
    summary = models.TextField(max_length=1500)
    image = models.ImageField(upload_to='images/')
    github_link = models.CharField(max_length=100)

    def __str__(self):
        return self.name
