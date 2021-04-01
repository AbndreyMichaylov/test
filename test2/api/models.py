from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Question(models.Model):
    TYPES_OF_ANSWER = (
        ('text', 'Ответ текстом'),
        ('onew', 'Ответ с выбором одного варианта'),
        ('many', 'Ответ с выбором нескольких вариантов'),
    )
    question_text = models.CharField(verbose_name='Текст вопроса', max_length=200)
    question_type = models.CharField(verbose_name='Тип ответа',max_length=4, choices=TYPES_OF_ANSWER)
    question_case = models.CharField(verbose_name='Варианты ответа', max_length=500, blank=True)

    def __str__(self):
        return self.question_text

class Survey(models.Model):
    STATUSES = (
        ('notend', 'Не пройден'),
        ('ended', 'Пройден'),
    )
    name = models.CharField(verbose_name='Название опроса',max_length=40)
    date_start = models.DateTimeField(verbose_name='Дата начала', auto_now_add=True)
    date_end = models.DateTimeField(verbose_name='Дата окончания', blank=True, null=True)
    desc = models.CharField(verbose_name='Описание',max_length=300)
    questions = models.ManyToManyField(verbose_name='Вопросы',to=Question)
    status = models.CharField(verbose_name='Статус',max_length=6, choices=STATUSES, default='n')
    copied = models.BooleanField(verbose_name='Копировано', default=False)

    def __str__(self):
        return self.name + ' | ' + str(self.copied)

class StartedSurvey(Survey):
    pass

class Answer(models.Model):
    survey = models.ForeignKey(verbose_name='Тест',to=StartedSurvey, on_delete=models.CASCADE)
    answer = models.CharField(verbose_name='Ответы',max_length=500, blank=True)
    def __str__(self):
        return self.survey.name



class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    answers = models.ManyToManyField(to=Answer, blank=True)

    def __str__(self):
        return self.user.username
