from django.shortcuts import render
from django.http import HttpResponse
from .models import Skill, User, Question
from rest_framework.views import APIView
from .serializers import QuestionSerializer
from rest_framework.response import Response
from rest_framework import status

def home(request):
    return HttpResponse("Hello World!")

class QuestionsAPI(APIView):
    def get(self,request, title, format=None):
        try:
            import pdb; pdb.set_trace()
            question =  Question.objects.get(question_title=title)
            question_serializer = QuestionSerializer(question)
            question_data = question_serializer.data
            return Response(question_data, status=status.HTTP_200_OK)
        except:
            return Response({'success': False, 'message': 'No Question with the given title found.'}, status=status.HTTP_400_BAD_REQUEST)
