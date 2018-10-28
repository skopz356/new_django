from django.contrib import admin

from .models import Page, Subject, Category

# Register your models here.

class SubjectInline(admin.StackedInline):
    model = Subject
    extra = 1

class CategoryAdmin(admin.ModelAdmin):
    inlines = [SubjectInline]


class PageAdmin(admin.ModelAdmin):
    list_display = ["title", "content"]

admin.site.register(Page, PageAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Subject)