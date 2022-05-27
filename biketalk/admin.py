from django.contrib import admin
from .models import Article, Opinion
# from django_summernote.admin import SummernoteModelAdmin


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    """ register decorator: article model """
    # customise list view of admin panel
    list_display = ('article_name', 'slug', 'status', 'created_on')
    # add search fields for either name or content
    search_fields = ['article_name', 'article_detail']
    # prepopulate slug field when completing title field
    prepopulated_fields = {'slug': ('article_name',)}
    # add filter for article status and created_by date
    list_filter = ('status', 'created_on')
    # summernote formatting
    summernote_fields = ('article_detail')


@admin.register(Opinion)
class OpinionAdmin(admin.ModelAdmin):
    """ register decorator: opinion class """
    list_display = ('name', 'body', 'article', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    # add an approved opinions section
    actions = ['approve_opinions']

    # to approve comment, Boolean=True
    def approve_opinions(self, request, queryset):
        queryset.update(approved=True)
