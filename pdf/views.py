from django.shortcuts import render
from django.http import FileResponse
from reportlab.pdfgen import canvas
from course.models import Project
from django.shortcuts import render
from io import BytesIO, StringIO

def pdf(request):
	return render(request, "pdf.html")

def generate_pdf(request):
	response = FileResponse(generate_pdf_file(), 
							as_attachment=True, 
							filename='Project.pdf')
	return response


def generate_pdf_file():
	

	buffer = BytesIO()
	p = canvas.Canvas(buffer)

	# Create a PDF document
	projects =Project.objects.all()
	p.drawString(100, 750, "Book Catalog")

	y = 700
	for prj in projects:
		p.drawString(100, y, f"student_name: {prj.student_name}")
		p.drawString(100, y - 20, f"project_title: {prj.project_title}")
		p.drawString(100, y - 40, f"project_language: {prj.project_language}")
		y -= 60

	p.showPage()
	p.save()

	buffer.seek(0)
	return buffer

import csv

def generate_csv_file():
    buffer = StringIO()
    writer = csv.writer(buffer)
    projects = Project.objects.all()
    writer.writerow(['Name','Project_title','Languages'])
    for project in projects:
        writer.writerow([project.student_name,project.project_title,project.project_language])
    buffer.seek(0)
    csv_bytes = BytesIO(buffer.getvalue().encode('utf-8'))
    return csv_bytes

def generate_csv(request):
    buffer = generate_csv_file()
    response = FileResponse(buffer, as_attachment=True, filename='project.csv')
    return response


        

