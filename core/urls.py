
from django.contrib import admin
from django.urls import path
from main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home_view),
    path('fan/',fan_view),
    path('fan/<int:pk>/', fan_tanlangan),
    path('fan/<int:pk>/delete/confirm/', fan_delete_confirm),
    path('fan/<int:pk>/delete/', fan_delete),
    path('yonalish/', yonalish_view),
    path('yonalish/<int:pk>/', yonalish_tanlangan),
    path('yonalish/<int:pk>/delete/confirm/', yonalish_delete_confirm),
    path('yonalish/<int:pk>/delete/', yonalish_delete),
    path('teacher/', teacher_view),
    path('teacher/<int:pk>/delete/confirm/', teacher_delete_confirm),
    path('teacher/<int:pk>/delete/', teacher_delete),

]
