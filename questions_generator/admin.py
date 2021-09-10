from django.contrib import admin
from . import models


@admin.register(models.Quizes)

class Quizes(admin.ModelAdmin):
	list_display = [
        'id', 
        'organization',
        'exam_title',
        'subject',
        'is_active'
        ]

class Options(admin.TabularInline):
    model = models.Options
    fields = [
        'option_title', 
        'is_right'
        ]

@admin.register(models.Questions)

class Questions(admin.ModelAdmin):
    fields = [
        'quiz',
        'question_type',
        'question_title',
        'question_level',
        ]
    list_display = [
        'question_title'
        ]
    inlines = [
        Options, 
        ] 

@admin.register(models.Options)

class OptionsAdmin(admin.ModelAdmin):
    list_display = [
        'question',
        'option_title', 
        'is_right', 
        ]