#coding:utf-8
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index (request):
    return HttpResponse("hello , you are at the poll's index !")



