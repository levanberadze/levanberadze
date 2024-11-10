from django.shortcuts import render, get_object_or_404, redirect
from .models import Course
from .forms import CourseForm, StudentForm


def course_list(request):
    courses = Course.objects.all()
    return render(request, 'course_list.html', {'courses': courses})


def course_detail(request, id):
    course = get_object_or_404(Course, id=id)
    if request.method == "POST":
        student_form = StudentForm(request.POST)
        if student_form.is_valid():
            student = student_form.save(commit=False)
            student.course = course
            student.save()
            return redirect('course_detail', id=course.id)
    return render(request, 'course_detail.html', {'course': course})


def course_create(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm()
    return render(request, 'course_form.html', {'form': form})


def course_update(request, id):
    course = get_object_or_404(Course, id=id)
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('course_detail', id=course.id)
    else:
        form = CourseForm(instance=course)
    return render(request, 'course_form.html', {'form': form})


def course_delete(request, id):
    course = get_object_or_404(Course, id=id)
    course.delete()
    return redirect('course_list')
