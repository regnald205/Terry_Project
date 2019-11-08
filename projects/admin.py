from django.contrib import admin
from .models import Projects



class ProjectsAdmin(admin.ModelAdmin):
    list_display=('id','title','is_published')
    list_display_links=('id','title')
    list_filter=('realtor',)
    list_editable=('is_published',)
    search_fields=('title','description','address')
    list_per_page=25

admin.site.register(Projects, ProjectsAdmin)



