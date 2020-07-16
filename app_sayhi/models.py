import django
from django.db import models
from django.utils.timezone import now

from django.urls import reverse  # Used to generate URLs by reversing

from django.contrib.auth.models import User
from datetime import date
import uuid,hashlib
import random
import time
def get_unique_str(length):
    uuid_str = str(uuid.uuid4())
    random.seed(time.time())
    offset = random.randrange(1, 30)
    md5 = hashlib.md5()
    random.seed(time.time())
    md5.update(uuid_str.encode('utf-8'))
    return md5.hexdigest()[offset:length+offset]

# student 学生
# 信誉分动态生成
class student(models.Model):
    studentId = models.AutoField(primary_key=True)
    studentAlias = models.CharField(max_length=20,unique=True)
    studentPwd = models.CharField(max_length=20,default='66666666')
    studentPhone = models.CharField(max_length=12,default='13713800000')
    studentGender = models.BooleanField(default=True)
    studentAvatar = models.FilePathField(path='sayhi/avatar/',unique=True)# 具体设置还要查\
    objects = models.manager.QuerySet

# teacher 老师
# 信誉分动态生成
class teacher(models.Model):
    teacherId = models.AutoField(primary_key=True)
    teacherAlias = models.CharField(max_length=20,unique=True)
    teacherPwd = models.CharField(max_length=20,default='66666666')
    teacherPhone = models.CharField(max_length=12,default='13713800000')
    teacherGender = models.BooleanField(default=True)
    teacherAvatar = models.FilePathField(path='sayhi/avatar/',unique=True)# 具体设置还要查\
    objects = models.manager.QuerySet


# 课程
class course(models.Model):
    coId = models.AutoField(primary_key=True)

    # teacher
    coTID = models.CharField(max_length=8)
    # 课程简介
    coIntro = models.CharField(max_length=144,blank=True,null=True)
    coTime = models.DateTimeField(default=now())

    objects = models.manager.QuerySet




# 首页留言板
class message(models.Model):
    msId = models.AutoField(primary_key=True)
    msTID = models.CharField(max_length=8,default='')
    msSID = models.CharField(max_length=8,default='')
    # 只能有一个有值 不能全部有值：）

    msText = models.CharField(max_length=144,blank=True,null=True)
    msLikeCount = models.SmallIntegerField(default=0)
    msDisLikeCount = models.SmallIntegerField(default=0)
    msTime = models.DateTimeField(default=now())

    objects = models.manager.QuerySet



# star 师生通过课程 互相打分
class star(models.Model):
    starId = models.AutoField(primary_key=True)
    # 老师对学生
    starT2S = models.SmallIntegerField(default=5)

    # 学生对老师
    starS2T = models.SmallIntegerField(default=5)

    # teacher ID
    starTId = models.CharField(max_length=8)
    # student ID
    starSId = models.CharField(max_length=8)
    # course 课程ID
    starCId = models.CharField(max_length=8)

    objects = models.manager.QuerySet


# 师生通过课程互相评价
class comment(models.Model):
    cmId = models.AutoField(primary_key = True)
    cmText = models.CharField(max_length=144,default="还行")
    # 老师对学生
    cmT2S = models.SmallIntegerField(default=5)

    # 学生对老师
    cmS2T = models.SmallIntegerField(default=5)

    # teacher ID
    cmTId = models.CharField(max_length=8)
    # student ID
    cmSId = models.CharField(max_length=8)
    # course 课程ID
    cmCId = models.CharField(max_length=8)

    cmTime = models.DateTimeField(default=now())
    objects = models.manager.QuerySet
# 当courseID缺省 则是直接在其首页进行的评价
