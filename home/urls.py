from django.urls import path
from .views import index, student_list
from course.views import course_list

urlpatterns = [
    path("",index,name='home'),
    path("list_stu/",student_list ,name='list'),
]
    


