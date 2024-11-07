from django.db import models
import zipfile
import os
import re

def extrair_arquivo(zip_path, nome_jogo):
    """Descompacta arquivos ZIP para um diretório com o nome do jogo e retorna o caminho do diretório."""

    # Normaliza o nome do jogo para criar uma pasta segura
    nome_pasta = re.sub(r'[^\w\s-]', '', nome_jogo).strip().replace(' ', '_')
    destino_dir = os.path.join("media", "arquivos_extracao", nome_pasta)

    # Cria o diretório de destino, se ele não existir
    os.makedirs(destino_dir, exist_ok=True)

    # Verifica se o arquivo é ZIP e realiza a extração
    if zipfile.is_zipfile(zip_path):
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(destino_dir)
        print(f"Arquivo ZIP extraído para {destino_dir}")
    else:
        print("Formato de arquivo não suportado (somente ZIP permitido).")

    # Retorna o caminho do diretório onde os arquivos foram extraídos
    return destino_dir


# Create your models here.
class Jogo(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(max_length=200)
    imagem = models.ImageField(upload_to='imagens/') 
    arquivo = models.FileField(upload_to='arquivos/')
    diretorio = models.CharField(max_length=255, null=True, blank=True) 

    def __str__(self):
        return self.nome

    @classmethod
    def adicionar_jogo(
        cls,
        nome,
        descricao,
        imagem,
        arquivo,
    ):
        """Método para adicionar um novo jogo."""

        jogo = cls(
            nome=nome,
            descricao=descricao,
            imagem=imagem,
            arquivo=arquivo,
        )
        jogo.save()

        arquivo_path = jogo.arquivo.path

        
        diretorio_extraido = extrair_arquivo(arquivo_path, nome)
        jogo.diretorio = diretorio_extraido.replace("\\", "/")

        jogo.save()

        return jogo

    @classmethod
    def excluir_jogo(cls, jogo_id):
        """Método para excluir um jogo pelo ID."""
        try:
            jogo = cls.objects.get(id=jogo_id)
            jogo.delete()
            return True  # Retorna True se a exclusão foi bem-sucedida
        except cls.DoesNotExist:
            return False  # Retorna False se o jogo não foi encontrado

