# Utilized Code from Django-3-Tutorial created in IT394 class to get proper view of GraduationYear to DistinguishedGraduates
from django.contrib import admin
from django.urls import include, path

from . import views

# Utilized Code from Django-3-Tutorial created in IT394 class to get proper view of GraduationYear to DistinguishedGraduates
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results')
]
