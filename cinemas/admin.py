from django.contrib import admin
from .models import Cinema, Sala, Formato

admin.site.register([Cinema, Sala, Formato])
