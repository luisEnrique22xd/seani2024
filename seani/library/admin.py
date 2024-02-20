from django.contrib import admin

from .models import Module, Question


class QuestionInline(admin.StackedInline):
    model = Question


@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'num_question']
    inlines = [QuestionInline]

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question_text', 'module', 'correct']
    ordering = ['module']

# admin.site.register(Module, ModuleAdmin,QuestionInline)
# admin.site.register(Question, QuestionAdmin)
# Register your models here.
