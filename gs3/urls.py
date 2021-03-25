
from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Student/', views.studentlist.as_view()),

    path('Student/<int:pk>/', views.studentlist.as_view()), 
    path('add_comment/',views.add_comment),
    path('comment/', views.CommentAPI.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)