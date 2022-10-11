from rest_framework import viewsets

from .serializer import SurveySerializer, SurveyQuestionSerializer, SurveyQuestionAlternativeSerializer
from .models import Survey, SurveyQuestion, SurveyQuestionAlternative


class SurveyViewSet(viewsets.ModelViewSet):
    queryset = Survey.objects.prefetch_related('questions__alternatives')
    serializer_class = SurveySerializer


class SurveyQuestionViewSet(viewsets.ModelViewSet):
    queryset = SurveyQuestion.objects.prefetch_related('alternatives')
    serializer_class = SurveyQuestionSerializer


class SurveyQuestionAlternativeViewSet(viewsets.ModelViewSet):
    queryset = SurveyQuestionAlternative.objects.all()
    serializer_class = SurveyQuestionAlternativeSerializer
