from django.contrib import admin
from poll.models import Question, Choice

class choiceInline(admin.TabularInline):
    model = Choice
    extra = 1

class question_model_admin(admin.ModelAdmin):
    list_display = ('question', 'created_at')
    fieldsets = [
        (None, {'fields': ['question']})
    ]
    inlines = [choiceInline]

admin.site.register(Question, question_model_admin)
