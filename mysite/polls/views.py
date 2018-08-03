from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader

from .models import Question, Choice

def index(request):
    latest_question_list = Question.objects.order_by('pk')[:5]
    choice_list = Choice.objects.order_by('id')
    list = []
    result = ""
    for q in latest_question_list:
    	result = result + "<br>" + str(q.id) +". "+q.question_text + "<br>"
    	choice = "&emsp;Choices :<br> &emsp;"
    	for c in choice_list:
    		if str(c.question) == str(q.question_text):
    			choice = choice + c.choice_text + ", "
    	result = result + choice

    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/details.html', {'question': question})

def results(request, question_id, results):
    response = "You're looking at the %s of question %s."
    return HttpResponse(response % (results, question_id))

def vote(request, question_id):

    return HttpResponse("You're voting on question %s." % question_id)
