from django.contrib import admin

from .models import Clubs,Projects,Reports
# Register your models here.

admin.site.register(Clubs)
admin.site.register(Projects)
admin.site.register(Reports)