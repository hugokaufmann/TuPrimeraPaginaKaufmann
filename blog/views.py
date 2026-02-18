from django.shortcuts import render, redirect
from .forms import AutorForm, PostForm, ComentarioForm
from .models import Post

# Create your views here.
def inicio(request):
    return render(request, "blog/inicio.html")

def crear_autor(request):
    if request.method == "POST":
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = AutorForm()

    return render(request, 'blog/formulario.html', {'form': form, 'titulo': 'Crear Autor'})

def crear_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = PostForm()

    return render(request, 'blog/formulario.html', {'form': form, 'titulo': 'Crear Post'})


def crear_comentario(request):
    if request.method == "POST":
        form = ComentarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = ComentarioForm()

    return render(request, 'blog/formulario.html', {'form': form, 'titulo': 'Crear Comentario'})


def buscar_post(request):
    resultados = []
    if request.GET.get("q"):
        query = request.GET.get("q")
        resultados = Post.objects.filter(titulo__icontains=query)

    return render(
        request,
        "blog/buscar_post.html",
        {"resultados": resultados},
    )

