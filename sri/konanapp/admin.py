from django.contrib import admin
from .models import license_DB, license_DBAdmin 
admin.site.register(license_DB,license_DBAdmin)
