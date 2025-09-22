from django.contrib import admin
from .models import *
from django.contrib.auth.models import User, Group

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id','name','age','gender','daraja', 'fan')
    list_display_links = ('id','name')
    search_fields = ('name',)

class YonalishAdmin(admin.ModelAdmin):
    list_display = ('id','nom','active')
    list_display_links = ('id','nom')
    list_ordering = ('active',)
    search_fields = ('nom',)

class FanAdmin(admin.ModelAdmin):
    list_display = ( 'id',"nom","asosiy","yonalish",)
    list_display_links = ('id','nom')
    list_filter = ('asosiy', 'yonalish')
    search_fields = ('nom',)

admin.site.register(Yonalish, YonalishAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Fan, FanAdmin)
admin.site.unregister([User, Group])
