from django.contrib import admin
from .models import *

@admin.register(message)
class student_admin(admin.ModelAdmin):
    list_display=('name','phone','city','state','message')

