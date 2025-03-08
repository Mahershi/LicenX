from django.contrib import admin
from .models import User, Project, Subscriptions, Instance
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('email',)}),
        (_('Personal Info'), {'fields': ('name',)}),
        (_('Permission'), {'fields': ('is_superuser',)}),
    )

    add_fieldsets = (
        (None, {'fields': ('email', 'password1', 'password2',)}),
        (_('Personal Info'), {'fields': ('name',)}),
        (_('Permission'), {'fields': ('is_superuser', 'is_staff',)}),
    )

    list_display = ('id', 'name', 'email',)
    list_filter = ('is_superuser', 'is_staff',)
    filter_horizontal = ()
    search_fields = ('name', 'email',)
    ordering = ('name',)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('identity', 'user', 'created_at')}),
    )

    add_fieldsets = (
        (None, {'fields': ('identity', 'user', 'created_at',)}),
    )

    list_display = ('id', 'identity', 'user', 'created_at')
    list_filter = ('user',)
    filter_horizontal = ()
    search_fields = ('identity',)
    ordering = ('identity',)


@admin.register(Instance)
class InstanceAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('project', 'hwid', 'domain')}),
    )

    add_fieldsets = (
        (None, {'fields': ('project', 'hwid', 'domain',)}),
    )

    list_display = ('id', 'project', 'hwid', 'domain')
    list_filter = ('project',)
    filter_horizontal = ()
    search_fields = ('project', 'hwid', 'domain')
    ordering = ('project',)


@admin.register(Subscriptions)
class SubscriptionAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('instance', 'expires', 'last_checkin')}),
        (_('Configuration'), {'fields': ('grace_period', 'checkin_interval', 'bypass')}),
    )

    add_fieldsets = (
        (None, {'fields': ('instance', 'expires', 'last_checkin')}),
        (_('Configuration'), {'fields': ('grace_period', 'checkin_interval', 'bypass')}),
    )

    list_display = ('id', 'instance', 'expires', 'last_checkin', 'grace_period', 'checkin_interval', 'bypass')
    list_filter = ('instance', 'expires', 'last_checkin', 'bypass')
    filter_horizontal = ()
    search_fields = ('instance',)
    ordering = ('instance', 'expires',)


