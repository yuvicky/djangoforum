from django.shortcuts import redirect
from django.shortcuts import render
from django.utils import timezone
from .models import Question
from django.shortcuts import render, get_object_or_404
from .forms import QuestionForm
from .forms import AnswerForm


# Create your views here.
def question_detail(request, pk):
	question = get_object_or_404(Question, pk=pk)
	return render(request, 'boldHER/question_detail.html', {'question': question})

def question_list(request):
    questions = Question.objects.all()
    return render(request, 'boldHER/question_list2.html', {'questions': questions})

def question_new(request):
	if request.method == "POST":
		form = QuestionForm(request.POST)
		if form.is_valid():
			question = form.save(commit=False)
			question.author = request.user
			question.published_date = timezone.now()
			question.save()
			return redirect('question_detail', pk=question.pk)
	else:
		form = QuestionForm()
	return render(request, 'boldHER/question_edit.html', {'form': form})


def answer_new(request):
	if request.method == "POST":
		form = AnswerForm(request.POST)
		if form.is_valid():
			answer = form.save(commit=False)
			answer.author = request.user
			answer.published_date = timezone.now()
			answer.save()
			return redirect('answer_detail', pk=answer.pk)
	else:
		form = QuestionForm()
	return render(request, 'boldHER/question_edit.html', {'form': form})

def question_edit(request, pk):
    question = get_object_or_404(Question, pk=pk)
    if request.method == "POST":
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.published_date = timezone.now()
            question.save()
            return redirect('question_detail', pk=question.pk)
    else:
        form = QuestionForm(instance=question)
    return render(request, 'boldHER/question_edit.html', {'form': form})

def answer_edit(request, pk):
    answer = get_object_or_404(Answer, pk=pk)
    if request.method == "POST":
        form = AnswerForm(request.POST, instance=answer)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user
            answer.published_date = timezone.now()
            answer.save()
            return redirect('answer_detail', pk=answer.pk)
    else:
        form = AnswerForm(instance=answer)
    return render(request, 'boldHER/answer_edit.html', {'form': form})
