from django.contrib import admin
from . import models


@admin.register(models.Test)
class TestAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'order_code',
        'is_visible',
    )

    list_filter = (
        'is_visible',
    )


@admin.register(models.Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = (
        'title',
    )


@admin.register(models.Variant)
class VariantAdmin(admin.ModelAdmin):
    list_display = (
        'title',
    )


@admin.register(models.Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = (
        'recruit',
        'test',
        'question',
        'variant',
    )

    list_filter = (
        'recruit__name',
        'test__title',
    )


@admin.register(models.Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = (
        'recruit',
        'test',
        'mark_as_pass',
        'datetime_of_completion',
    )

    list_filter = (
        'recruit__name',
        'test__title',
        'mark_as_pass',
    )
