from django.contrib import admin
from .models import Hello

class HelloAdmin(admin.ModelAdmin):
  list_display = ('title', 'description')

# Register your models here.
admin.site.register(Hello, HelloAdmin)
