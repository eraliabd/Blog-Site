from django.contrib import admin
from .models import Post, Comment, SendMessage, Category


class CommentInline(admin.StackedInline):  # StackedInline and TabularInline commentni chiroyli ko'rish uchun
    model = Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')
    inlines = [
        CommentInline
    ]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')


@admin.register(SendMessage)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'message', 'created')
    list_filter = ('created', 'updated')
    search_fields = ('name', 'email', 'subject', 'message')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name',)
    list_filter = ('category_name',)
    search_fields = ('category_name',)
