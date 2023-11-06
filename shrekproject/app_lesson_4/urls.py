from django.urls import path
from .view import lesson

urlpatterns = [
    path('lesson_4', lesson),
]