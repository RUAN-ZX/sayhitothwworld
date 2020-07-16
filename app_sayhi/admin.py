from django.contrib import admin
from .models import student,teacher,message,comment,course,star

# Register your models here.
admin.site.register(student)
admin.site.register(teacher)
admin.site.register(message)
admin.site.register(comment)
admin.site.register(course)
admin.site.register(star)
