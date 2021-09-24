from django.urls import path
from .views import QuizesList,UpCommingQuiz,QuizQuestion,QuestionSection,QuestionOperation,AnswerSection,AnswerOperation,QuizOpertion,QuickQuizAccess,ResultView

urlpatterns = [
    path('dashboard/', QuizesList.as_view()), #does display all active quizes and also add quizes
    path('upcomming_quizes/', UpCommingQuiz.as_view()), #does display all active quizes and also add quizes
    path('quiz_operation/<int:pk>/',QuizOpertion.as_view()),
    path('participate/<int:search>/', QuizQuestion.as_view()), #does display all questions and options under a quiz
    path('quick_access/<str:code>/', QuickQuizAccess.as_view()), #does display all questions and options under a quiz
    path('add_questions/<int:pk>/', QuestionSection.as_view()), #does add and also read question
    path('question_operations/<int:pk>/', QuestionOperation.as_view()), #does read update or delete question
    path('add_answers/<int:pk>/', AnswerSection.as_view()), #does add and also read option
    path('answers_operations/<int:pk>/', AnswerOperation.as_view()), #does read update or delete option
    path('leaderboard/<int:pk>/', ResultView.as_view()),# Result API
]


""" 
http://127.0.0.1:8000/quiz/dashboard/
http://127.0.0.1:8000/quiz/quiz_operation/4/
http://127.0.0.1:8000/quiz/upcomming_quizes/
http://127.0.0.1:8000/quiz/quick_access/password/
http://127.0.0.1:8000/quiz/participate/15/
http://127.0.0.1:8000/quiz/add_questions/3/
http://127.0.0.1:8000/quiz/question_operations/15/
http://127.0.0.1:8000/quiz/add_answers/15/
http://127.0.0.1:8000/quiz/answers_operations/15/
http://127.0.0.1:8000/quiz/leaderboard/4/

"""