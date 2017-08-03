from django.shortcuts import render
from django.utils import timezone
from .models import Question

# Create your views here.
def question_list(request):
    questions = Question.objects.all()
    return render(request, 'boldHER/question_list2.html', {'questions': questions})