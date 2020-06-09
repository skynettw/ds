from django.contrib import admin
from mysite import models

class StoryAdmin(admin.ModelAdmin):
	list_display = ('sno', 'title')

admin.site.register(models.Story, StoryAdmin)