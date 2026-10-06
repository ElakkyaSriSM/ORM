from django.db import models
from django.contrib import admin
class license_DB(models.Model):
    license_no = models.CharField(primary_key=True, max_length=20)
    name = models.CharField(max_length=20)
    Dob = models.DateField()
    issueDate = models.DateField()
    fathersName = models.CharField(max_length=20)
    bloodgrp = models.CharField(max_length=5)
    address = models.TextField()

class license_DBAdmin(admin.ModelAdmin):
    list_display = ["license_no","name","Dob","issueDate","fathersName","bloodgrp","address"]


