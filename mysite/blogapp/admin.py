
from django.contrib import admin
from .models import Author, Category, Tag, Article

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'author', 'category')
    search_fields = ('title', 'content')
    list_filter = ('pub_date', 'author', 'category', 'tags')
    date_hierarchy = 'pub_date'


    raw_id_fields = ('author', 'category', 'tags')

admin.site.register(Author, AuthorAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Article, ArticleAdmin)

