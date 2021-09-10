from rest_framework import serializers
from .models import Quizes, Questions, Options

class AllQuizesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Quizes
        fields = '__all__'

class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Questions
        fields = "__all__"
        extra_kwargs = {'"quiz"': {'required': False}}



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
