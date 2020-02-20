from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
# Utilized Code from Django-3-Tutorial created in IT394 class to get proper view of GraduationYear to DistinguishedGraduates
def index(request):
    return HttpResponse("Under Construction")

def detail(request, question_id):
    return HttpResponse("You're looking at Graduation Year %s." % question_id)

def results(request, question_id):
    response = "You're looking at the Distinguished Graduates of Graduation Year %s."
    return HttpResponse(response % question_id)
