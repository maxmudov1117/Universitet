from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import *

def home_view(request):
    return render(request,"home.html")

def fan_view(request):

    if request.method == 'POST':
        Fan.objects.create(
            nom = request.POST.get('nom'),
            asosiy = request.POST.get('asosiy') if request.POST.get('asosiy') else 0,
            yonalish = get_object_or_404(Yonalish, id = request.POST.get('yonalish_id')),
        )
        return redirect('/fan/')
    fanlar = Fan.objects.all()
    yonalishlar = Yonalish.objects.all()

    search = request.GET.get('search')
    if search:
        fanlar = fanlar.filter(nom__contains=search)
    context = {
        "fanlar":fanlar,
        'search':search,
        'yonalishlar':yonalishlar,
    }
    return render(request,"fan.html", context)

def fan_tanlangan(request,pk):
    fan = get_object_or_404(Fan,pk=pk)
    context = {
        'fan':fan,
    }
    return render(request,"tanlangan_fan.html", context)

def fan_delete_confirm(request,pk):
    fan = get_object_or_404(Fan,pk=pk)
    context = {
        'fan':fan,
    }
    return render(request,"fan_delete_confirm.html", context=context)

def fan_delete(request,pk):
    fan = get_object_or_404(Fan, pk=pk)
    fan.delete()
    return redirect("/fan/")

def yonalish_view(request):

    if request.method == 'POST':
        Yonalish.objects.create(
            nom = request.POST.get('nom'),
            active = request.POST.get('active') if request.POST.get('active') else 1,
        )
        return redirect('/yonalish/')
    yonalishlar = Yonalish.objects.all()
    context = {
        "yonalishlar":yonalishlar,
    }
    return render(request,"yonalish.html", context)

def yonalish_tanlangan(request,pk):
    yonalish = get_object_or_404(Yonalish,pk=pk)
    context = {
        'yonalish':yonalish,
    }
    return render(request,"tanlangan_yonalish.html", context)

def yonalish_delete_confirm(request,pk):
    yonalish = get_object_or_404(Yonalish,pk=pk)
    context = {
        'yonalish':yonalish,
    }
    return render(request,"yonalish_delete_confirm.html", context=context)

def yonalish_delete(request,pk):
    yonalish = get_object_or_404(Yonalish, pk=pk)
    yonalish.delete()
    return redirect("/yonalish/")

def teacher_view(request):

    if request.method == 'POST':
        Teacher.objects.create(
            name = request.POST.get('name'),
            age = request .POST.get('age'),
            gender = request.POST.get('gender'),
            daraja = request.POST.get('daraja'),
            fan = get_object_or_404(Fan, id=request.POST.get('fan_id'))
        )
    teachers = Teacher.objects.all()
    search = request.GET.get('search')
    fanlar = Fan.objects.all()
    if search:
        teachers = teachers.filter(name__contains=search)
    context = {
        "teachers":teachers,
        'search':search,
        'fanlar':fanlar,
    }
    return render(request,"teacher.html", context)

def teacher_delete_confirm(request,pk):
    teacher = get_object_or_404(Teacher,pk=pk)
    context = {
        'teacher':teacher,
    }
    return render(request,"teacher_delete_confirm.html", context=context)

def teacher_delete(request,pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    teacher.delete()
    return redirect("/teacher/")
