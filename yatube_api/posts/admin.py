from django.contrib import admin

from .models import Comment, Group, Post


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = (
        'slug',
        'description'
    )
    search_fields = ('title',)
    list_filter = ('title', 'slug',)
    empty_value_display = '-пусто-'


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'text',
        'pub_date',
        'author',
        'group',
    )
    search_fields = ('text',)
    list_editable = ('group',)
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'post',
        'author',
        'text',
        'created'
    )

    list_editable = ('author',)
    list_filter = ('author',)
    list_per_page = 10
    search_fields = ('text',)
