from django.contrib import admin

# Register your models here.
from django.contrib import admin
from models import Question, Choice


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('text info', {'fields':['question_text']}),
        ('Date information', {'fields':['pub_date'], 'classes': ['collapse']})
    ]
    list_display = ('question_text', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)

