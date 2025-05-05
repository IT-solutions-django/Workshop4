from django.contrib import admin
from .models import Article, ArticleCategory


@admin.register(ArticleCategory)
class ArticleCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_filter = ('category', 'created_at')
    search_fields = ('name', 'subtitle', 'content')
    prepopulated_fields = {'slug': ('name',)}
