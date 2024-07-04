from django.shortcuts import render, HttpResponse
from .models import Student
from course.models import Course



def index(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        dob = request.POST.get('dob')
        gender = request.POST.get('gender')
        classes = request.POST.get('classes')
        regcode = request.POST.get('regcode')

        Student.objects.create( #creates when u enter
            name = name,
           email = email,
            dob = dob,
            regcode = regcode,
            gender = gender,
            classes = classes
        )

        return HttpResponse("<h3>Successful Registration✅</h3>")
    return render(request, 'index.html')

    
    

def student_list(request):
    queryset = Student.objects.all()
    if request.GET.get('class'):
        queryset = queryset.filter(classes__icontains = request.GET.get('class'))

    context = {
        'students' : queryset 
    }
    return render(request, 'list.html', context)

# def course_list(request):
#     queryset2 = Course.objects.all()
#     # if request.GET.get('class'):
#     #     queryset2 = queryset2.filter(course_name__icontains = request.GET.get('class'))
#     context = { 'courses' : queryset2 }
#     return render(request, 'list.html', context)

