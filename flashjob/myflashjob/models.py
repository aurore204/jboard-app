from django.db import models

# Create your models here.
class Job(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    company = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    posted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
#from myflashjob.models import Job
#job = Job(
 #   title="Développeur Django",
 #   description="Développement d'applications web avec Django.",
 #   company="TechCorp",
 #   location="Paris",
#)
#job.save()