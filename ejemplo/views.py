from django.shortcuts import render

def index(request):
    return render(request, "ejemplo/saludar.html")


def saludar_a(request, nombre):
    return render(request, 
    'ejemplo/saludar_a.html',
    {"nombre": nombre}
    )


def sumar(request, a, b):
    return render (request, 
    'ejemplo/sumar.html', 
    {"a": a,
     "b": b,
     "resultado": a + b
    }
    )
