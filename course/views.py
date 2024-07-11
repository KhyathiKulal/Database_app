from django.shortcuts import render, HttpResponse
from course.models import Course, Project

def course_list(request):
    queryset = Course.objects.all()
    if request.GET.get('class'):
        queryset = queryset.filter(course_name__icontains = request.GET.get('class'))
    
    context = {
        'courses' : queryset
    }
    return render(request, 'course.html', context)

def ProjectForm(request):
    if request.method == "POST":
        student_name = request.POST.get('name')
        project_title = request.POST.get('projectTitle')
        project_language = request.POST.get('lang')
        duration = request.POST.get('duration')
        obj=Project(student_name=student_name,project_title=project_title,project_language=project_language,duration=duration)
        obj.save()
      
        return HttpResponse("<h3>Project details saved</h3>")
    return render(request, 'projectForm.html')

def project_details(request):
    projects = Project.objects.all()
    context = {
        'project' : projects 
    }
    return render(request, 'project.html', context)


