from django.shortcuts import render, redirect, get_object_or_404
from .models import Teacher
from .forms import TeacherForm

def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'teacher_list.html', context={'teachers': teachers})

def teacher_create(request):
    if request.method == "POST":
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("teacher_list")
    return render(request, 'teacher_create.html', context={'form': TeacherForm()})

def teacher_update(request, id):
    teacher = Teacher.objects.get(id=id)
    if request.method == "POST":
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect("teacher_list")
    return render(request, 'teacher_create.html', context={'form': TeacherForm(instance=teacher)})

def teacher_delete(request, id):
    teacher = Teacher.objects.get(id=id)
    teacher.delete()
    return redirect("teacher_list")









