from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    # 데이터 필드
    website = models.CharField(verbose_name="웹사이트", max_length=256, null=True)
    bio = models.CharField(verbose_name="자기소개", max_length=256, null=True)
    phone = models.CharField(verbose_name="전화번호", max_length=13, null=True) # -포함 010-xxxx-xxxx
    name = models.CharField(max_length=30, null=True)

    class Meta:
        db_table = 'user'
