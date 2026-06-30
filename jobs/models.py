from django.db import models

class Job(models.Model):

    job_id = models.CharField(max_length=50, unique=True)

    title = models.CharField(max_length=200)

    experience_level = models.CharField(max_length=50)

    years_of_experience = models.CharField(max_length=20)

    skills = models.TextField()

    responsibilities = models.TextField()

    keywords = models.TextField()

    def __str__(self):
        return self.title