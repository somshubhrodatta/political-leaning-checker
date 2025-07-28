from django.db import models
from django.contrib.auth.models import User

class UserResponse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    question_1 = models.IntegerField()
    question_2 = models.IntegerField()
    question_3 = models.IntegerField()
    question_4 = models.IntegerField()
    question_5 = models.IntegerField()
    question_6 = models.IntegerField()
    question_7 = models.IntegerField()
    question_8 = models.IntegerField()
    question_9 = models.IntegerField()
    question_10 = models.IntegerField()
    question_11 = models.IntegerField()
    question_12 = models.IntegerField()
    question_13 = models.IntegerField()
    question_14 = models.IntegerField()
    question_15 = models.IntegerField()
    question_16 = models.IntegerField()
    question_17 = models.IntegerField()
    question_18 = models.IntegerField()
    question_19 = models.IntegerField()
    question_20 = models.IntegerField()
    score = models.FloatField()
    label = models.CharField(max_length=20)
    comparison = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username if self.user else 'Anonymous'} -> {self.label}"