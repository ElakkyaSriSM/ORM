# Ex02 Django ORM Web Application
## Date: 06.10.26

## AIM
To develop a Django Application to store and retrieve data from a Vehicle Service Database platform using Object Relational Mapping(ORM).




## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Detect changes and create migration files that describe how to modify the database schema

### STEP 5:
Execute the migration files and update the database schema to match your Django models

### STEP 6:
Create a superuser with full access rights to all models and data through the admin interface.

### STEP 7:
Apply the migration files of the created app to the database

### STEP 8:
Execute Django admin using localhost and create details for 10 entries

## PROGRAM

```
models.py

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


admin.py

from django.contrib import admin
from .models import license_DB, license_DBAdmin 
admin.site.register(license_DB,license_DBAdmin)
```


## OUTPUT
![alt text](image.png)


## RESULT
Thus the program for creating Online Food Delivery Database using ORM hass been executed successfully
