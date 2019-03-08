from rest_framework import serializers
from .models import User, Question, Skill, Tag, Answer

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('user', 'question_title', 'question_description', 'question_upvotes', 'question_downvotes')
