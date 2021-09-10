from django.db import models
from datetime import datetime
from django.utils.translation import gettext_lazy as translate

class Quizes(models.Model):
    organization = models.CharField(max_length=400, default="Test Examination")
    exam_title = models.CharField(max_length=200, default="New Quiz")
    subject = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    total_time = models.FloatField(max_length=6)
    start = models.DateTimeField()
    end = models.DateTimeField()
    is_active = models.BooleanField(default=False)
    access_password = models.CharField(max_length=100,blank=True, unique=True)

    def __str__(self):
        return self.exam_title


class Questions(models.Model):
    level =(
        (1, translate('Easy')),
        (2, translate('Medium')),
        (3, translate('Hard')),
        (4, translate('Advanced')),
    )

    q_type = (
        (1, translate('Writing')),
        (2, translate('Multiple Choice')),
    )

    question_type = models.IntegerField(
        choices=q_type, default=1)
    question_title = models.CharField(max_length=300)
    question_level = models.IntegerField(
        choices=level, default=1)
    created_at = models.DateTimeField(
        auto_now_add=True)
    quiz = models.ForeignKey(
        Quizes, related_name="question",  on_delete=models.CASCADE)

    def __str__(self):
        return self.question_title


class Options(models.Model):
    question = models.ForeignKey(
        Questions, related_name="answer", on_delete=models.CASCADE)
    option_title = models.CharField(
        max_length=300)
    is_right = models.BooleanField(default=False)

    def __str__(self):
        return self.option_title
