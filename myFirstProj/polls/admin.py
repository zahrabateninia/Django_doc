from django.contrib import admin
from .models import Question

# admin.site.register(Question)
# customize the admin form: 
class QuestionAdmin(admin.ModelAdmin):
    fields = ["pub_date", "question_text"]


admin.site.register(Question, QuestionAdmin)