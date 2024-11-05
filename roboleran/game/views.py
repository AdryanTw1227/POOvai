from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Jogo, Asset
from django.views.decorators.csrf import csrf_exempt

def index(request):
    if request.method == 'POST':
        # Coletando os dados do formulário
        nome = request.POST.get('Name')
        descricao = request.POST.get('Description')
        imagem = request.FILES.get('Image') 
        arquivo = request.FILES.get('Package') 
        
        
        Jogo.adicionar_jogo(nome=nome, descricao=descricao, imagem=imagem, arquivo=arquivo)

        messages.success(request, 'Jogo adicionado com sucesso!')

        return redirect('jogos/')  
    return render(request, 'inicio/index.html')

def jogos(request):
    return render(request, 'inicio/jogos.html')

def sobre(request):
    return render(request, 'inicio/sobre.html')

@csrf_exempt
def asset(request): 
    if request.method == 'POST':
        assets = request.FILES.getlist('asset[]')

        for asset in assets: 
            Asset.adicionar_asset(file= asset)

        messages.success(request, 'Asset created Succesfully (_))ZZD !')
    return render(request, 'inicio/index.html')

