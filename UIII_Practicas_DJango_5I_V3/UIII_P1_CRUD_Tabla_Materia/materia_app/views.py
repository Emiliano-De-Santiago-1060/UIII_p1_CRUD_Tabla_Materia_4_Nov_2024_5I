from django.shortcuts import render, redirect
from .models import Materia
# Create your views here.

def inicio_vista(request):
    lasmaterias=Materia.objects.all()

    return render(request, "gestionarMateria.html", {"mismaterias":lasmaterias})

def registrarMateria(request):
    codigo=request.POST["txtcodigo"]
    nombre=request.POST["txtnombre"]
    credits=request.POST["numcreditos"]
    guardarmateria=Materia.objects.create(codigo=codigo, nombre=nombre, credits=credits)
    return redirect("/")

def seleccionarMateria(request, codigo):
    materia=Materia.objects.get(codigo=codigo)
    return render(request, "editarMateria.html", {"mismaterias":materia})

def borrarMateria(request, codigo):
    materia=Materia.objects.get(codigo=codigo)
    materia.delete()
    return redirect("/")

def editarMateria(request):
    codigo=request.POST["txtcodigo"]
    nombre=request.POST["txtnombre"]
    credits=request.POST["numcreditos"]
    materia=Materia.objects.get(codigo=codigo)
    materia.nombre=nombre
    materia.credits=credits
    materia.save()
    return redirect("/")