from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from .models import Jogo
from django.views.decorators.csrf import csrf_exempt

def index(request):
    if request.method == 'POST':
        # Coletando os dados do formulário
        nome = request.POST.get('Name')
        descricao = request.POST.get('Description')
        imagem = request.FILES.get('Image') 
        arquivo = request.FILES.get('Package')
        
        print(nome)
        
        
        Jogo.adicionar_jogo(
            nome=nome,
            descricao=descricao,
            imagem=imagem,
            arquivo=arquivo,
        )

        messages.success(request, 'Jogo adicionado com sucesso!')

        return redirect('jogos/')  
    jogos = Jogo.objects.all()
    
    return render(request, 'inicio/index.html', {'jogos': jogos})

def jogos(request):
    jogos = Jogo.objects.all()

    return render(request, 'inicio/jogos.html', {'jogos': jogos})

def sobre(request):
    return render(request, 'inicio/sobre.html')
