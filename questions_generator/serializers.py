from rest_framework import serializers
from .models import Quizes, Questions, Options, Result

class AllQuizesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Quizes
        fields = '__all__'
        extra_kwargs = {'organization': {'required': False},'exam_title': {'required': False},'subject': {'required': False},'description': {'required': False}, 'total_time': {'required': False}, 'start': {'required': False}, 'end': {'required': False}, 'is_active': {'required': False}, 'access_password': {'required': False}}


class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Questions
        fields = "__all__"
        extra_kwargs = {'quiz': {'required': False}}

class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Options
        fields = '__all__'
        extra_kwargs = {'question': {'required': False}, 'option_title':{'required':False}}

class QuestionAndOptionSerializer(serializers.ModelSerializer):

    answer = AnswerSerializer(many=True, read_only=True)
    class Meta:
        model = Questions
        fields = [
            'id',
            'question_title',
            'question_type',
            'question_level',
            'answer'
        ]
        extra_kwargs = {'question': {'required': False}, 'option_title':{'required':False}}


class QuizInfoSerializers(serializers.ModelSerializer):

    quiz = AllQuizesSerializer(read_only=True)

    class Meta:
    
        model = Questions
        fields = [
            'quiz'
        ]


class ResultSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Result
        fields = '__all__'
        extra_kwargs = {'participant': {'required': False}, 'quiz_id': {'required': False}, 'feedback':{'required':False}}
