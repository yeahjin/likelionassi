from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUserModel(AbstractUser):
    GENDER = (
        ("M", "남자"),
        ("F", "여자"),
    )
    #둘다 true인 경우 -> 로그인에 상관이 없는 경우
    birthday = models.DateField(blank = True, null =True)
    gender = models.CharField(max_length = 2, blank = True, null = True,choices=GENDER)