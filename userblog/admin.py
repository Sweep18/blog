from django.contrib import admin

from .models import News, CommentNews


class NewsAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'title', 'image')
    list_filter = ('date',)


admin.site.register(News, NewsAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'news', 'comment')
    list_filter = ('date',)


admin.site.register(CommentNews, CommentAdmin)