from django.contrib import admin
from .models import Post

# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """
    Class modifies and customises how the model Post is displayed.
    list_display - attribute which sets the fields of the model
    @admin.register() - decorator which performs the same role as admin.site.register() function which was replaced
    with it, registering the ModelAdmin class that it decorates.
    list_filter - creates a filter box allowing to filter the results by the fields included in the attributes.
    search_fields - adds a search box to search through the searchable fields.
    prepopulated_fields - allows to prepopulate slug with text from the title.
    raw_id_fields - adds lookup widget to find and select the author when putting the post in.
    date_hierarchy - adds nav links to navigate through the dates.
    ordering - specified default sorting criteria.
    """
    list_display = ['title', 'slug', 'author', 'publish', 'status']
    list_filter = ['status', 'created', 'publish', 'author']
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ['author']
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']
