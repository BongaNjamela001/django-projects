from django.contrib import admin

# Register your models here.

from .models import (
    Contact,
    Resume,
    Portfolio
)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name' )

@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name' )

@admin.register(Portfolio)
class Portfolio(admin.ModelAdmin):
    list_display = ('id', 'name' )
    readonly_fields = ('slug',)