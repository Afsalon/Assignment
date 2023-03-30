from django.contrib import admin
from content.models import Category,Content
# Register your models here.

class CategoryModelAdmin(admin.ModelAdmin):
    model = Category
    list_display = ( 'name', 'created_date')

class ContentModelAdmin(admin.ModelAdmin):
    model = Content
    list_display = ('title', 'user', 'category')

admin.site.register(Category,CategoryModelAdmin)
admin.site.register(Content,ContentModelAdmin)