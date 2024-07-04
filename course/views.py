from django.shortcuts import render, HttpResponse
from course.models import Course

def course_list(request):
    queryset = Course.objects.all()
    if request.GET.get('class'):
        queryset = queryset.filter(course_name__icontains = request.GET.get('class'))
    
    context = {
        'courses' : queryset
    }
    return render(request, 'course.html', context)

# def ProjectForm(request):
#     if request.method == "POST":
#         name = request.POST.get('name')
#         projectTitle = request.POST.get('projectTitle')
#         language = request.POST.get('lang')
#         duration = request.POST.get('duration')

#         Project.objects.create( #creates when u enter
#             student_name = name,
#             project_title = projectTitle,
#             project_language = language,
#             duration = duration,
#         )

#         return HttpResponse("<h3>Project details saved</h3>")
#     return render(request, 'projectForm.html')

# def project_details(request):
#     projects = Project.objects.all()
#     context = {
#         'project' : projects 
#     }
#     return render(request, 'project.html', context)

