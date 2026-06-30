import os
import json
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from jobs.models import Job

with open("dataset/jobs.json", "r", encoding="utf-8") as file:
    jobs = json.load(file)

for item in jobs:

    Job.objects.create(

        job_id=item["JobID"],

        title=item["Title"],

        experience_level=item["ExperienceLevel"],

        years_of_experience=item["YearsOfExperience"],

        skills=", ".join(item["Skills"]),

        responsibilities=", ".join(item["Responsibilities"]),

        keywords=", ".join(item["Keywords"]),

    )

print("Jobs imported successfully!")