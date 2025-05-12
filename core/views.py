from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import FormularioHabilidade
from .models import HabilidadeUsuario

def home(request):
    return render(request, 'core/home.html')

def adicionar_habilidade(request):
    if request.method == 'POST':
        form = FormularioHabilidade(request.POST)
        if form.is_valid():
            habilidade_usuario = form.save(commit=False)
            habilidade_usuario.usuario = request.user
            habilidade_usuario.save()
            return redirect('minhas_habilidades')
    else:
        form = FormularioHabilidade()
    
    return render(request, 'core/adicionar_habilidade.html', {'form': form})

@login_required
def minhas_habilidades(request):
    # Busca todas as habilidades cadastradas por este usuário
    habilidades = HabilidadeUsuario.objects.select_related('habilidade', 'habilidade__categoria').filter(usuario=request.user)

    # Organiza por categoria para exibir agrupado
    habilidades_por_categoria = {}
    for habilidade_usuario in habilidades:
        categoria = habilidade_usuario.habilidade.categoria.nome
        if categoria not in habilidades_por_categoria:
            habilidades_por_categoria[categoria] = []
        habilidades_por_categoria[categoria].append(habilidade_usuario)

    return render(request, 'core/minhas_habilidades.html', {
        'habilidades_por_categoria': habilidades_por_categoria
    })