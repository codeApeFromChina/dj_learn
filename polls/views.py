# coding:utf-8
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from polls.models import Question
from django.template import RequestContext, loader


def index(request):
    try:
        last_question = Question.objects.all().order_by('-pub_date')[:5]
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    context = {
        'last_question_list' : last_question,
    }
    return render(request,'polls/index.html', context)


def results(request, question_id):
    print(1111111)
    return render(question_id)


def detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question':question})


def vote(request, question_id):
    print(33333)
    return render(question_id)
