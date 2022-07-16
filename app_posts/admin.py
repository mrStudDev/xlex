from django.contrib import admin

from .models import PostsXlex, Category


class PostAdmin(admin.ModelAdmin):
    list_display = ["__str__", "data"]
    list_filter = ["data"]
    search_fields = ["title", "content"]
    prepopulated_fields = {"slug": ("title",)}

    class Meta:
        model = PostsXlex


admin.site.register(PostsXlex, PostAdmin)
admin.site.register(Category)
