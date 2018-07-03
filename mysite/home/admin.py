from django.contrib import admin

from .models import Page, Subject, Category

# Register your models here.

class SubjectInline(admin.StackedInline):
    model = Subject
    extra = 1

class CategoryAdmin(admin.ModelAdmin):
    inlines = [SubjectInline]

admin.site.register(Page)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Subject)