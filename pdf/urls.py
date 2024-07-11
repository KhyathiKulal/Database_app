from django.urls import path
from .views import generate_pdf, generate_pdf_file, pdf, generate_csv, generate_csv_file

urlpatterns = [

    path("button/", pdf, name='pdf'),
    path("file/", generate_pdf_file, name='file'),
    path("generate_pdf/", generate_pdf, name='pdf'),
    path("generate_csv/", generate_csv, name='csv_generate'),
    path("csv/", generate_csv_file, name='csv'),
]