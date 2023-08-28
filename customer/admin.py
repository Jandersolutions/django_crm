from django.contrib import admin
from .models import Cliente

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'telefone', 'tipo_cliente', 'status_conta')
    list_filter = ('tipo_cliente', 'status_conta')
    search_fields = ('nome', 'email', 'telefone')
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('nome', 'cargo', 'empresa', 'email', 'telefone', 'endereco')
        }),
        ('Detalhes do Cliente', {
            'fields': ('data_inicio_relacionamento', 'tipo_cliente', 'status_conta')
        }),
        ('Informações Demográficas', {
            'fields': ('idade', 'genero', 'localizacao')
        }),
        ('Atividades e Interações', {
            'fields': ('historico_interacoes', 'historico_compras', 'fonte_aquisicao', 'campanhas_marketing', 'tarefas')
        }),
        ('Preferências e Interesses', {
            'fields': ('interesses', 'historico_suporte')
        }),
        ('Outras Informações', {
            'fields': ('tags', 'perfil_social')
        }),
    )

