from django.shortcuts import render
import os
import random
from time import time
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import uuid,hashlib
from .models import student
from .models import teacher
import json
def get_unique_str():
    uuid_str = str(uuid.uuid4())
    md5 = hashlib.md5()
    md5.update(uuid_str.encode('utf-8'))
    return md5.hexdigest()

def storing(t,request,cmd):
    if cmd==1:
        # 用户头像
        cmdstr = 'avatar'
    else:
        # preface 课程首页：）
        cmdstr = 'preface'
    #print('p1')
    fileI = request.FILES.get(cmdstr, None)
    #print('p2')
    fileNameI = fileI.name.split('.')
    if not fileI:
        return -1
    filename = fileNameI[0] + str(t) + '.' + fileNameI[1]
    #print('p3')
    try:
        storing = open(os.path.join('media/',cmdstr,filename), 'wb+')
    except Exception as e:
        print(e)
        storing=''
        return -1
        #print(os.path.join('media/',cmdstr,filename))
    for chunk in fileI.chunks():
        storing.write(chunk)
    storing.close()
    print(filename + 'storing oK')
    return filename


# 首页 通过Alias创建用户以及message
# 预先预存100张头像：）
def createAliasStudentMessage(request):
    t = int(time())
    dictJson = {}
    studentI = student()
    if request.method == "POST":
        try:
            studentI.studentAlias = request.POST.get('alias')
            studentI.studentGender = request.POST.get('gender')
            studentI.studentPhone = request.POST.get('phone')
            studentI.studentPwd = request.POST.get('password')
            if student.objects.filter(studentAlias=studentI.studentAlias):
                dictJson['code'] = -1
                return JsonResponse(dictJson)
            if student.objects.filter(studentPhone=studentI.studentPhone):
                dictJson['code'] = -2
                return JsonResponse(dictJson)
            print('33')
            avatar = storing(t, request, 1)
            # if not avatar:
            #     dictJson['code'] = -3
            #     return JsonResponse(dictJson)
            studentI.studentAvatar = avatar
            studentI.save()
            return render(request, 'artalk_uploadstudentResult.html', context={"student": studentI})
        except AttributeError:
            dictJson['code'] = -3
            return JsonResponse(dictJson)
        except Exception as e:
            print(e)
            dictJson['code'] = -4
            return JsonResponse(dictJson)
    else:
        return render(request, 'sayhi_uploadStudent.html')

# 通过注册登录生成的学生
def createStudent(request):
    t = int(time())
    dictJson = {}
    studentI = student()
    if request.method == "POST":
        try:
            studentI.studentAlias = request.POST.get('alias')
            studentI.studentGender = request.POST.get('gender')
            studentI.studentPhone = request.POST.get('phone')
            studentI.studentPwd = request.POST.get('password')
            if student.objects.filter(studentAlias=studentI.studentAlias):
                dictJson['code'] = -1
                return JsonResponse(dictJson)
            if student.objects.filter(studentPhone=studentI.studentPhone):
                dictJson['code'] = -2
                return JsonResponse(dictJson)
            print('33')
            avatar = storing(t, request, 1)
            # if not avatar:
            #     dictJson['code'] = -3
            #     return JsonResponse(dictJson)
            studentI.studentAvatar = avatar
            studentI.save()
            return render(request, 'artalk_uploadstudentResult.html', context={"student": studentI})
        except AttributeError:
            dictJson['code'] = -3
            return JsonResponse(dictJson)
        except Exception as e:
            print(e)
            dictJson['code'] = -4
            return JsonResponse(dictJson)
    else:
        return render(request, 'sayhi_uploadStudent.html')

# 通过审批得到的老师
def createTeacher(request):
    t = int(time())
    dictJson = {}
    teacherI = teacher()
    if request.method == "POST":
        try:
            teacherI.teacherAlias = request.POST.get('alias')
            teacherI.teacherGender = request.POST.get('gender')
            teacherI.teacherPhone = request.POST.get('phone')
            teacherI.teacherPwd = request.POST.get('password')
            if teacher.objects.filter(teacherAlias=teacherI.teacherAlias):
                dictJson['code'] = -1
                return JsonResponse(dictJson)
            if teacher.objects.filter(teacherPhone=teacherI.teacherPhone):
                dictJson['code'] = -2
                return JsonResponse(dictJson)
            print('33')
            avatar = storing(t, request, 1)
            # if not avatar:
            #     dictJson['code'] = -3
            #     return JsonResponse(dictJson)
            teacherI.teacherAvatar = avatar
            teacherI.save()
            return render(request, 'artalk_uploadteacherResult.html', context={"teacher": teacherI})
        except AttributeError:
            dictJson['code'] = -3
            return JsonResponse(dictJson)
        except Exception as e:
            print(e)
            dictJson['code'] = -4
            return JsonResponse(dictJson)
    else:
        return render(request, 'sayhi_uploadTeacher.html')


