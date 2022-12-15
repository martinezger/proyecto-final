from django.shortcuts import render
from django.views.generic import ListView, CreateView
from ejemplo_dos.models import Post
from django.urls import reverse_lazy

def index(request):
    return render(request, "ejemplo_dos/index.html", {})


class PostList(ListView):
    model = Post  

class PostCrear(CreateView):
    model = Post
    success_url = reverse_lazy("ejemplo-dos-listar")
    fields = '__all__'
    

