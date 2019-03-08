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



class TagsAPI(APIView):
    def get(self,request, tag, format=None):
        try:
            import pdb; pdb.set_trace()
            tag =  Tag.objects.get(tag=tag)
            tag_serializer = TagSerializer(tag)
            tag_data = tag_serializer.data
            return Response(tag_data, status=status.HTTP_200_OK)
        except:
            return Response({'success': False, 'message': 'No tag found.'}, status=status.HTTP_400_BAD_REQUEST)

class QuestionsAPI(APIView):
    def get(self,request, skill, format=None):
        try:
            import pdb; pdb.set_trace()
            skill =  Skill.objects.get(skill=skill)
            skill_serializer = SkillSerializer(skill)
            skill_data = skill_serializer.data
            return Response(skill_data, status=status.HTTP_200_OK)
        except:
            return Response({'success': False, 'message': 'No such skill found.'}, status=status.HTTP_400_BAD_REQUEST)

class QuestionsAPI(APIView):
    def get(self,request, title, format=None):
        try:
            import pdb; pdb.set_trace()
            answer =  answer.objects.get(answer_text=title)
            answer_serializer = AnswerSerializer(answer)
            answer_data = answer_serializer.data
            return Response(answer_data, status=status.HTTP_200_OK)
        except:
            return Response({'success': False, 'message': 'No Question with the given title found.'}, status=status.HTTP_400_BAD_REQUEST)
