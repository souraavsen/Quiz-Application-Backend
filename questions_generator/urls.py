from django.urls import path
from .views import QuizesList,UpCommingQuiz,QuizQuestion,QuestionSection,QuestionOperation,AnswerSection,AnswerOperation


urlpatterns = [
    path('dashboard/', QuizesList.as_view()), #does display all active quizes and also add quizes
    path('upcomming_quiz/', UpCommingQuiz.as_view()), #does display all active quizes and also add quizes
    path('participate/<int:search>/', QuizQuestion.as_view()), #does display all questions and options under a quiz
    path('create_questions/<int:pk>/', QuestionSection.as_view()), #does add and also read question
    path('question_operations/<int:pk>/', QuestionOperation.as_view()), #does read update or delete question
    path('add_answers/<int:pk>/', AnswerSection.as_view()), #does add and also read option
    path('answers_operations/<int:pk>/', AnswerOperation.as_view()), #does read update or delete option
]