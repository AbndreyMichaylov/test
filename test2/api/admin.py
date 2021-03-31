from django.contrib import admin
from . import models


admin.site.register(models.Question)
admin.site.register(models.Person)
admin.site.register(models.Answer)
admin.site.register(models.StartedSurvey)

class SurveysAdmin(admin.ModelAdmin):
    list_filter = ['copied']

admin.site.register(models.Survey,SurveysAdmin)