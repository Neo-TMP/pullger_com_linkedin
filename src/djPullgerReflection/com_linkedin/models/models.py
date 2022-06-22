from django.db import models
from .models_companies import companies

class people(models.Model):
    uuid = models.CharField(max_length=36, primary_key = True) 
    id = models.IntegerField(blank=False, null=False)

    first_name = models.CharField(max_length=150, null=True)
    second_name = models.CharField(max_length=150, null=True)
    full_name = models.CharField(max_length=300, null=True)

    url = models.CharField(max_length=300, null=True)
    discription = models.CharField(max_length=300, null=True)

    location = models.CharField(max_length=300, null=True)

    date_small_loaded = models.DateField(null=True)
    date_full_loaded = models.DateField(null=True)

class people_experience(models.Model):
    uuid = models.CharField(max_length=36, primary_key = True)
    people = models.ForeignKey(people, verbose_name = 'uuid_people', db_column='uuid_people', to_field = 'uuid', on_delete=models.CASCADE)
    companies = models.ForeignKey(companies, verbose_name = 'uuid_companies', db_column='uuid_companies', to_field = 'uuid', on_delete=models.CASCADE)
    job_discription = models.CharField(max_length=300, null=True)
    job_timing_type = models.CharField(max_length=50, null=True)
    date_small_loaded = models.DateField(null=True)
