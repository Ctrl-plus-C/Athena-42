from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Skill, User, Question, Answer, Tag, Skill, Bider
from rest_framework.views import APIView
from .serializers import QuestionSerializer, AnswerSerializer, SkillSerializer, TagSerializer, BiderSerializer
from rest_framework.response import Response
from rest_framework import status
from .forms import CustomUserForm
import json

def dashboard(request):
    if request.user.is_authenticated():
        first_name = request.user.first_name
        last_name = request.user.last_name
        name = first_name+" "+last_name
        return render(request, 'education/dashboard.html', {'name':name})
    return redirect('/accounts/login')

def notif(request):
    if request.user.is_authenticated():
        return render(request, 'education/notif.html')
    return redirect('/accounts/login')

def userprofile(request):
    if request.user.is_authenticated():
        bio = request.user.bio
        first_name = request.user.first_name
        last_name = request.user.last_name
        name = first_name+" "+last_name
        skills = Skill.objects.filter(user=request.user).values()
        if request.method == 'POST':
            user_form = CustomUserForm(request.POST)
            if user_form.is_valid():
                userform_data = user_form.save(commit=False)
                userform_data.user = request.user
                userform_data.save()
                return redirect('/')
        else:
            instance = User.objects.get(username=request.user.username)
            user_form = CustomUserForm(instance=instance)
        return render(request, 'education/userprofile.html',{'form':user_form, 'name':name, 'bio':bio, 'skills':skills})
    return redirect('/')            

def postquestion(request):
    first_name = request.user.first_name
    last_name = request.user.last_name
    name = first_name+" "+last_name
    return render(request, 'education/postquestion.html', {'name':name})

def answerquestion(request):
    first_name = request.user.first_name
    last_name = request.user.last_name
    name = first_name+" "+last_name
    return render(request, 'education/answerquestion.html',{'name':name})

def listedquestion(request):
    questions = Question.objects.filter(user=request.user).values()
    return render(request, 'education/listedquestion.html',{'question':questions})

class QuestionsAPI(APIView):
    def get(self, request, format=None):
        try:
            question = Question.objects.all()
            question_serializer = QuestionSerializer(question, many=True)
            question_data = question_serializer.data
            return Response(question_data, status=status.HTTP_200_OK)
        except:
            return Response({'success': False, 'message': 'No Question with the given title found.'}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, format=None):
        question_serializer = QuestionSerializer(data=request.data)
        if question_serializer.is_valid():
            question_serializer.save()
            return Response(question_serializer.data, status=status.HTTP_201_CREATED)
        return Response(question_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, format=None):
        try:
            question = Question.objects.get(
                question_title=request.data.get('question_query'))
        except:
            return Response({'success': False, 'message': 'No such question found'})
        question_serializer = QuestionSerializer(
            question, data=request.data, partial=True)
        if question_serializer.is_valid():
            question_serializer.save()
            return Response(question_serializer.data, status=status.HTTP_200_OK)
        return Response(question_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TagsAPI(APIView):
    def get(self, request, question, format=None):
        try:
            tag = Tag.objects.filter(question=question)
            tag_serializer = TagSerializer(tag, many=True)
            tag_data = tag_serializer.data
            return Response(tag_data, status=status.HTTP_200_OK)
        except:
            return Response({'success': False, 'message': 'No tag found.'}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, format=None):
        request_data = request.data.getlist('data')[0]
        request_data = eval(json.loads(json.dumps(request_data)))
        tag_serializer = TagSerializer(data=request_data, many=True)
        if tag_serializer.is_valid():
            tag_serializer.save()
            return Response(tag_serializer.data, status=status.HTTP_201_CREATED)
        return Response(tag_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, format=None):
        try:
            tag = Tag.objects.get(question=request.data.get('question_id'), pk=request.data.get('tag_pk'))
        except:
            return Response({'success': False, 'message': 'No such tag found'}, status=status.HTTP_400_BAD_REQUEST)
        tag_serializer = TagSerializer(tag, data=request.data, partial=True)
        if tag_serializer.is_valid():
            tag_serializer.save()
            return Response(tag_serializer.data, status=status.HTTP_200_OK)
        return Response(tag_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SkillAPI(APIView):
    def get(self, request, user, format=None):
        try:
            skill = Skill.objects.filter(user=user)
            skill_serializer = SkillSerializer(skill, many=True)
            skill_data = skill_serializer.data
            return Response(skill_data, status=status.HTTP_200_OK)
        except:
            return Response({'success': False, 'message': 'No such skill found.'}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, format=None):
        skill_serializer = SkillSerializer(data=request.data)
        if skill_serializer.is_valid():
            skill_serializer.save()
            return Response(skill_serializer.data, status=status.HTTP_201_CREATED)
        return Response(skill_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, format=None):
        try:
            skill = Skill.objects.get(user=request.data.get('user'), name=request.data.get('query_skill'))
        except:
            return Response({'success':False, 'message': 'Requested skill doesn\'t exists.'}, status=status.HTTP_400_BAD_REQUEST)
        skill_serializer = SkillSerializer(skill, data=request.data, partial=True)
        if skill_serializer.is_valid():
            skill_serializer.save()
            return Response(skill_serializer.data, status=status.HTTP_200_OK)
        return Response(skill_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AnswerAPI(APIView):
    def get(self, request, question_id, format=None):
        try:
            answer = Answer.objects.filter(question=question_id)
            answer_serializer = AnswerSerializer(answer, many=True)
            answer_data = answer_serializer.data
            return Response(answer_data, status=status.HTTP_200_OK)
        except:
            return Response({'success': False, 'message': 'No Answer found.'}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, format=None):
        answer_serializer = AnswerSerializer(data=request.data)
        if answer_serializer.is_valid():
            answer_serializer.save()
            return Response(answer_serializer.data, status=status.HTTP_200_OK)
        return Response(answer_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, question_id, format=None):
        try:
            # here question_id will contain user id, its a misleading name used to prevent creation of another url.
            answer = Answer.objects.get(question=request.data.get(
                'answer_question'), user=question_id)
        except:
            return Response({'success': False,'message':'No Answer for user found.'}, status=status.HTTP_400_BAD_REQUEST)
        answer_serializer = AnswerSerializer(answer, data=request.data, partial=True)
        if answer_serializer.is_valid():
            answer_serializer.save()
            return Response(answer_serializer.data, status=status.HTTP_200_OK)
        return Response(answer_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BiderAPI(APIView):
    def get(self, request, question_id, format=None):
        try:
            bider = Bider.objects.filter(question=question_id)
            bider_serializer = BiderSerializer(bider, many=True)
            bider_data = bider_serializer.data
            return Response(bider_data, status=status.HTTP_200_OK)
        except:
            return Response({'success': False, 'message': 'No bider found.'}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, format=None):
        bider_serializer = BiderSerializer(data=request.data)
        if bider_serializer.is_valid():
            bider_serializer.save()
            return Response(bider_serializer.data, status=status.HTTP_200_OK)
        return Response(bider_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def put(self, request, question_id, format=None):
    #     try:
    #         # here question_id will contain user id, its a misleading name used to prevent creation of another url.
    #         answer = Answer.objects.get(question=request.data.get(
    #             'answer_question'), user=question_id)
    #     except:
    #         return Response({'success': False,'message':'No Answer for user found.'}, status=status.HTTP_400_BAD_REQUEST)
    #     answer_serializer = AnswerSerializer(answer, data=request.data, partial=True)
    #     if answer_serializer.is_valid():
    #         answer_serializer.save()
    #         return Response(answer_serializer.data, status=status.HTTP_200_OK)
    #     return Response(answer_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def get_userdata(request):
    user_id = request.POST.get('user')
    user = User.objects.get(pk=user_id)
    return JsonResponse({'name': user.first_name + " " + user.last_name,'reputation': user.reputation})