from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework import generics, status

from .models import Survey, Person, Answer, StartedSurvey
from .serializers import SurveySerializer,AnswerSerializer, AnswerOneSerializer
import json


class ListEndedSurvey(APIView):

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        user = Person.objects.get(user=request.user)
        print(user)
        answers = user.answers.all()
        survs = []
        for answer in answers:
            survey = answer.survey
            if survey.status == 'ended' and survey.copied == True:
                survs.append(survey)
        s1 = SurveySerializer(survs, many=True)
        s2 = AnswerSerializer(answers, many=True)
        return Response({'surveys' : s2.data})

class SurveyAll(generics.ListAPIView):
    queryset = Survey.objects.filter(copied=False).all()
    serializer_class = SurveySerializer
    permission_classes = [permissions.IsAuthenticated]

class AnswerAll(generics.ListAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerOneSerializer
    permission_classes = [permissions.IsAuthenticated]
    

class StartOpros(APIView):

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):

        survey_id = request.data['survey']
        answer = request.data['answer']

        survey = Survey.objects.get(id=survey_id)
        questions = survey.questions.all()
        print(questions)
        survey.pk = None
        survey.copied = True
        survey.status = 'ended'
        startedsurvey = StartedSurvey.objects.create(
            name=survey.name,
            date_start=survey.date_start,
            date_end=survey.date_end,
            desc=survey.desc,
            status='ended',
            copied=True
        )
        startedsurvey.save()
        for q in questions:
            startedsurvey.questions.add(q)
        new_answer = Answer.objects.create(
            survey = startedsurvey,
            answer = answer
        )
        new_answer.save()
        _user = request.user
        _person = Person.objects.get(user=_user)
        _person.answers.add(new_answer)

        """
        serializer = AnswerOneSerializer(data=request.data)       
        serializer.is_valid(raise_exception=True)
        serializer.save()
        """

        return Response({'ok': json.dumps('ok')})