from django.shortcuts import render, HttpResponse

def home2(request):
    return HttpResponse('<h1>hello</h1>')

def about(request):
    return HttpResponse('<h1>hello</h1>')

def home1(request):
    return HttpResponse('<h1>hello</h1>')
