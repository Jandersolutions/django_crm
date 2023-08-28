from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100, blank=True, null=True)
    empresa = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    endereco = models.TextField(blank=True, null=True)
    data_inicio_relacionamento = models.DateField()
    tipo_cliente = models.CharField(max_length=20, choices=[
        ('potencial', 'Potencial'),
        ('atual', 'Atual'),
        ('antigo', 'Antigo'),
    ])
    status_conta = models.CharField(max_length=20, choices=[
        ('ativo', 'Ativo'),
        ('inativo', 'Inativo'),
        ('suspenso', 'Suspenso'),
    ])
    idade = models.PositiveIntegerField(blank=True, null=True)
    genero = models.CharField(max_length=10, blank=True, null=True)
    localizacao = models.CharField(max_length=100, blank=True, null=True)
    historico_interacoes = models.TextField(blank=True, null=True)
    historico_compras = models.TextField(blank=True, null=True)
    fonte_aquisicao = models.CharField(max_length=100, blank=True, null=True)
    campanhas_marketing = models.TextField(blank=True, null=True)
    tarefas = models.TextField(blank=True, null=True)
    interesses = models.TextField(blank=True, null=True)
    historico_suporte = models.TextField(blank=True, null=True)
    tags = models.TextField(blank=True, null=True)
    perfil_social = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.nome

