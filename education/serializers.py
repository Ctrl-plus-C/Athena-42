from rest_framework import serializers
from .models import User, Question, Skill, Tag, Answer, Bider

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('pk','user', 'question_title', 'question_description', 'question_upvotes', 'question_downvotes')

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('user','question', 'answer_text', 'answer_upvotes', 'answer_downvotes')

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('tag', 'question')

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ('user', 'name')

class BiderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bider
        fields = ('user', 'question')

