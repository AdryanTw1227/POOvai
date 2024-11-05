from django.db import models

# Create your models here.

class Asset(models.Model):
    file = models.FileField(upload_to='assets2/')

    def __str__(self):
        return('')
    
    @classmethod
    def adicionar_asset(cls, file):
        ass = cls(file=file)
        ass.save()
        return ass
    


class Jogo(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(max_length=200)
    imagem = models.ImageField(upload_to='imagens/') 
    arquivo = models.FileField(upload_to='arquivos/')
    assets = models.ForeignKey(Asset, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

    @classmethod
    def adicionar_jogo(cls, nome, descricao, imagem, arquivo):
        """Método para adicionar um novo jogo."""
        jogo = cls(nome=nome, descricao=descricao, imagem=imagem, arquivo=arquivo)
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

