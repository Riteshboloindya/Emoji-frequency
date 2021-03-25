from django.contrib import admin
from .models import Student,Comment

# Register your models here.
admin.site.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display =['id','name', 'roll','city']
    


class CommentAdmin(admin.ModelAdmin):
    list_display=['id','text']
    search_fields=['text']
    
admin.site.register(Comment,CommentAdmin)