from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    skills = models.CharField(max_length=300, blank=True, default="")
    project_url = models.URLField(blank=True, null=True)
    github_url = models.URLField(blank=True, null=True)
    thumbnail = models.ImageField(upload_to='projects/', blank=True, null=True)

    def __str__(self):
        return self.title
