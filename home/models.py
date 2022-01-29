from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to="project images")
    project_url = models.URLField()
    description = models.TextField(default="lorem en lorem")


    def __str__(self):
        return self.title


class Resume(models.Model):
    title = models.CharField(max_length=50)
    curriculumvitae = models.FileField()

    def __str__(self):
        return self.title


class Contact(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()


    def __str__(self):
        return self.email