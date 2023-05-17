from django.contrib import admin
from blog.models import Post, Category

class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "created_date", "published_date", "author")


admin.site.register(Post, PostAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)


admin.site.register(Category, CategoryAdmin)
