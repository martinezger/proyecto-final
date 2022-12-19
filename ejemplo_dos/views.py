from django.shortcuts import render
from django.views.generic import (DetailView, ListView, CreateView, 
                                    UpdateView, DeleteView)
from ejemplo_dos.models import Post
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from ejemplo_dos.forms import UsuarioForm


def index_ejemplo_dos(request):
    return render(request, "ejemplo_dos/index.html", {})


class PostDetalle(DetailView):
    model = Post

class PostListar(ListView):
    model = Post  

class PostCrear(LoginRequiredMixin, CreateView):
    model = Post
    success_url = reverse_lazy("ejemplo-dos-listar")
    fields = '__all__'

class PostBorrar(DeleteView):
    model = Post
    success_url = reverse_lazy("ejemplo-dos-listar")

class PostActualizar(UpdateView):
    model = Post
    success_url = reverse_lazy("ejemplo-dos-listar")
    fields = "__all__"

class UserLogin(LoginView):
    next_page = reverse_lazy('ejemplo-dos-listar')

class UserLogout(LogoutView):
    next_page = reverse_lazy('ejemplo-dos-index')

class UserSignUp(CreateView):
    form_class = UsuarioForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('ejemplo-dos-listar')
