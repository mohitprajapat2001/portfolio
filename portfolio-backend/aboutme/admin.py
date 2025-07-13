# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import (
    Profile,
    Address,
    Resume,
    Skills,
    Technology,
    Project,
    Experience,
    ContactMessage,
)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "created",
        "modified",
        "first_name",
        "last_name",
        "email",
        "phone",
        "profile_picture",
    )
    list_filter = ("created", "modified")


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "created",
        "modified",
        "profile",
        "street_address",
        "city",
        "region",
        "country",
        "postal_code",
    )
    list_filter = (
        "created",
        "modified",
        "profile",
        "city",
        "region",
        "country",
    )


@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "created",
        "modified",
        "title",
        "description",
        "profile",
        "file",
        "is_primary",
    )
    list_filter = ("created", "modified", "profile", "is_primary")


@admin.register(Skills)
class SkillsAdmin(admin.ModelAdmin):
    list_display = ("id", "created", "modified", "profile", "name")
    list_filter = ("created", "modified", "profile")
    search_fields = ("name",)


@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "created",
        "modified",
        "profile",
        "image",
        "live_url",
        "source_url",
    )
    list_filter = ("created", "modified", "profile")
    raw_id_fields = ("technologies",)


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "role",
        "company",
        "start_date",
        "end_date",
        "description",
        "is_current",
    )
    list_filter = ("start_date", "end_date", "is_current")


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "created",
        "modified",
        "name",
        "email",
        "subject",
        "message",
    )
    list_filter = ("created", "modified")
    search_fields = ("name",)
