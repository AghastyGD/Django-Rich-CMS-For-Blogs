from django.contrib import admin
from .models import Post
from .models import Profile
from .models import Category
from ckeditor.widgets import CKEditorWidget
from django.db import models

class PostAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget},
    }
    list_display = ('title', 'category', 'published',)
    list_filter = ('category', 'published',)
    list_editable = ('published',)
    search_fields = ('title', 'content',)
    
admin.site.register(Post, PostAdmin)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    model = Profile

    
@admin.register(Category)
class TagAdmin(admin.ModelAdmin):
    model = Category
