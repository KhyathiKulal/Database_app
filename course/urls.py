from django.urls import path
from .views import course_list
urlpatterns = [
    path("course/",course_list,name='course'),
    # path("projectForm/",ProjectForm,name='PForm'),
    # path("projectDetails/",project_details,name='PDetails'),
]