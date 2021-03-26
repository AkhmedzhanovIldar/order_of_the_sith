from django.contrib import admin
from django.forms import CheckboxSelectMultiple
from .models import *

@admin.register(Planet)
class PlanetAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )

@admin.register(Recruit)
class RecruitAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'planet',
        'age',
        'email',
    )

    list_filter = ('planet',)

@admin.register(Sith)
class SithAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'planet',
    )

    list_filter = ('planet',)

class VariantInstanceInline(admin.TabularInline):
    model = Variant

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = (
        'title',
    )
    inlines = [VariantInstanceInline]

@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = (
        'order_code',
        'visible',
    )

    list_filter = ('visible',)

    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple}
    }

@admin.register(Variant)
class VariantAdmin(admin.ModelAdmin):
    list_display = (
        'question',
        'title',
    )

    list_filter = ('question',)

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = (
        'recruit',
        'test',
        'question',
        'variant',
    )

    list_filter = ('recruit__name','test__order_code')

@admin.register(ShadowHand)
class ShadowHandAdmin(admin.ModelAdmin):
    list_display = (
        'recruit',
        'sith',
    )

    list_filter = ('sith',)

@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = (
        'recruit',
        'test',
        'mark_as_pass'
    )

    list_filter = ('test__order_code', 'recruit__name')