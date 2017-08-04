from django.shortcuts import render
from django.utils import timezone
from .models import Question
from django.shortcuts import render, get_object_or_404

# Create your views here.
def question_detail(request, pk):
	question = get_object_or_404(Question, pk=pk)
	return render(request, 'boldHER/question_detail.html', {'question': question})

def question_list(request):
    questions = Question.objects.all()
    return render(request, 'boldHER/question_list2.html', {'questions': questions})