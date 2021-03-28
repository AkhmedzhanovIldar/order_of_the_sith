from django.contrib import admin
from . import models


@admin.register(models.Planet)
class PlanetAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )


@admin.register(models.Sith)
class Sith(admin.ModelAdmin):
    list_display = (
        'name',
        'planet',
    )

    list_filter = (
        'planet__name',
    )


@admin.register(models.Recruit)
class RecruitAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'planet',
        'age',
        'email',
    )

    list_filter = (
        'planet__name',
    )


@admin.register(models.ShadowHand)
class ShadowHandAdmin(admin.ModelAdmin):
    list_display = (
        'recruit',
        'sith',
    )

    list_filter = (
        'sith__name',
    )
