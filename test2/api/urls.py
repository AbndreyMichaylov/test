from django.contrib import admin
from django.urls import path, include

from .views import SurveyAll, ListEndedSurvey, StartOpros, AnswerAll


urlpatterns = [
    path('survey/all', SurveyAll.as_view()),
    #path('survey/pass/<int:pk>', ),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('surveys/ended/all', ListEndedSurvey.as_view()),
    path('survey/start/', StartOpros.as_view()),
    path('answer/one/', AnswerAll.as_view())
]
