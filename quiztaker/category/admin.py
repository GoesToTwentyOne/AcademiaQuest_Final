from django.contrib import admin
from category.models import CategoryModel
# Register your models here.
# admin.site.register(models.Category)
class CategoryModelAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':['category_name',]}
admin.site.register(CategoryModel,CategoryModelAdmin)