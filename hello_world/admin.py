from django.contrib import admin
from .models import Professor

@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ['nome', 'email']
    search_fields = ['nome', 'email']
