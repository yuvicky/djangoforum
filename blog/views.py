from django.shortcuts import render

# Create your views here.
def question_list(request):
    return render(request, 'blog/question_list.html', {})