from rest_framework.response import Response
from .models import Options, Quizes, Questions, Result
from .serializers import AllQuizesSerializer, QuestionAndOptionSerializer, QuizInfoSerializers,QuestionSerializer,AnswerSerializer,ResultSerializer
from rest_framework.views import APIView
from rest_framework import status
import time


def random_name():
    secondsSinceEpoch = time.time()
    timeObj = time.localtime(secondsSinceEpoch)
    return("%d%d%d%d%d%d" % (timeObj.tm_mday, timeObj.tm_mon, timeObj.tm_year, timeObj.tm_hour, timeObj.tm_min, timeObj.tm_sec))

class QuizesList(APIView):
    def get(self, request):
        allquizes = Quizes.objects.filter(is_active=True)
        if allquizes:
            serializer = AllQuizesSerializer(allquizes, many=True)
            return Response(serializer.data)
        return Response([], status=status.HTTP_404_NOT_FOUND)

    def post(self, request, format=None):
        
        if request.data['access_password'] == "":
            request.data['access_password'] = random_name()

        serializer = AllQuizesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

""" 
http://127.0.0.1:8000/quiz/dashboard/

{
    "organization": "Quiz1",
    "exam_title": "Quiz-2",
    "subject": "SWEE",
    "description": "",
    "total_time": 2.0,
    "start": "2021-09-11T12:00:00Z",
    "end": "2021-09-11T12:00:00Z",
    "is_active": false,
    "access_password": ""
}
"""

class QuizOpertion(APIView):
    def get(self,request,pk):
        searched_quiz = Quizes.objects.filter(id=pk)
        if searched_quiz:
            serializer = AllQuizesSerializer(searched_quiz, many=True)
            return Response(serializer.data)
        return Response([], status=status.HTTP_404_NOT_FOUND)

    def put(self,request,pk, formate=None):
        searched_quiz = Quizes.objects.get(id=pk)

        if request.data['access_password'] == "":
            request.data['access_password'] = random_name()

        serializer = AllQuizesSerializer(searched_quiz,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        quiz = Quizes.objects.get(id=pk)
        quiz.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UpCommingQuiz(APIView):
    def get(self, request):
        allquizes = Quizes.objects.filter(is_active=False)
        if allquizes:
            serializer = AllQuizesSerializer(allquizes, many=True)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)


class QuizQuestion(APIView):

    def get(self, request, search):
        data = []
        quiz = Questions.objects.filter(quiz__id=search)
        
        if quiz:
            serializer = QuestionAndOptionSerializer(quiz, many=True)
            quiz_details = QuizInfoSerializers(quiz, many=True)
            data.append(quiz_details.data[0])
            data.append(serializer.data)
            if len(quiz_details.data) == 0 and len(serializer.data) == 0:
                data = []
            return Response(data)
        return Response(status=status.HTTP_404_NOT_FOUND)


class QuickQuizAccess(APIView):

    def get(self, request, code, formate=None):
        data = []
        id = Quizes.objects.get(access_password=code)
        quiz = Questions.objects.filter(quiz__id = id.id)
        
        if quiz:
            serializer = QuestionAndOptionSerializer(quiz, many=True)
            quiz_details = QuizInfoSerializers(quiz, many=True)
            data.append(quiz_details.data[0])
            data.append(serializer.data)
            if len(quiz_details.data) == 0 and len(serializer.data) == 0:
                data = []
            return Response(data)
        return Response(status=status.HTTP_404_NOT_FOUND)



class QuestionSection(APIView):

    def get(self, request,pk):
        # quiz_item = Questions.objects.filter(id=pk)
        questions = Questions.objects.filter(quiz=pk)
        serializer = QuestionAndOptionSerializer(questions, many=True)
        return Response(serializer.data)
    
    def post(self, request, pk, format=None):
        request.data["quiz"]= pk
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
"""
http://127.0.0.1:8000/quiz/add_questions/3/

{
"question_type": 2,
"question_title": "What is the maximum possible length of an array?",
"question_level": 3
} 
"""

class QuestionOperation(APIView):

    def get(self, request, pk, format=None):
        answers =  Questions.objects.filter(id=pk)
        serializer = QuestionAndOptionSerializer(answers, many=True)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        item = Questions.objects.get(id=pk)
        serializer = QuestionAndOptionSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        question = Questions.objects.get(id=pk)
        question.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AnswerSection(APIView):
    def get(self, request, pk, format=None):
        answers =  Options.objects.filter(question=pk)
        serializer = AnswerSerializer(answers, many=True)
        return Response(serializer.data)

    def post(self, request, pk, format=None):
        request.data["question"] = pk
        serializer = AnswerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
""" 
http://127.0.0.1:8000/quiz/add_answers/8/

{
"option_title": "A. None of them.",
"is_right": true
}
"""

class AnswerOperation(APIView):

    def get(self, request, pk, format=None):
        answers =  Options.objects.filter(id=pk)
        serializer = AnswerSerializer(answers, many=True)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        item = Options.objects.get(id=pk)
        serializer = AnswerSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# http://127.0.0.1:8000/quiz/answers_operations/34/

# {
# "option_title": "C. 32",
# "is_right": false,
# }

    def delete(self, request, pk, format=None):
        option = Options.objects.get(id=pk)
        option.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# http://127.0.0.1:8000/quiz/answers_operations/34/
# DELETE Button


class ResultView(APIView):
    def get(self, request, pk, formate=None):

        all_results = Result.objects.filter(quiz_id=pk).order_by('-total_number')
        serializer =  ResultSerializer(all_results, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, pk, format=None):
        res = Result.objects.filter(quiz_id = pk, participant = request.data["participant"])
        if res:
            res.delete()
        
        request.data["participant"] = request.data["participant"]
        request.data["quiz_id"] = pk

        serializer = ResultSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

