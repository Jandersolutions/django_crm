from django import forms
from django.utils.html import mark_safe
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = [
            'nome',
            'cargo',
            'empresa',
            'email',
            'telefone',
            'endereco',
            'data_inicio_relacionamento',
            'tipo_cliente',
            'status_conta',
            'idade',
            'genero',
            'localizacao',
            'historico_interacoes',
            'historico_compras',
            'fonte_aquisicao',
            'campanhas_marketing',
            'tarefas',
            'interesses',
            'historico_suporte',
            'tags',
            'perfil_social',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Adicione ícones do FontAwesome aos labels dos campos
        self.fields['nome'].label = mark_safe('<i class="fas fa-user"></i> nome ')
        self.fields['cargo'].label = mark_safe('<i class="fas fa-briefcase"></i> cargo ')
        self.fields['empresa'].label = mark_safe('<i class="fas fa-building"></i> empresa ')
        self.fields['email'].label = mark_safe('<i class="fas fa-envelope"></i> email')
        self.fields['telefone'].label = mark_safe('<i class="fas fa-phone"></i> telefone ')
        self.fields['endereco'].label = mark_safe('<i class="fas fa-map-marker-alt"></i> endereco ')
        self.fields['data_inicio_relacionamento'].label = mark_safe(' <i class="fas fa-calendar-alt"></i> data_inicio_relacionamento')
        self.fields['tipo_cliente'].label = mark_safe(' <i class="fas fa-users"></i> tipo_cliente')
        self.fields['status_conta'].label = mark_safe('<i class="fas fa-id-card"></i> status_conta ')
        self.fields['idade'].label = mark_safe(' <i class="fas fa-birthday-cake"></i> idade')
        self.fields['genero'].label = mark_safe(' <i class="fas fa-venus-mars"></i> genero')
        self.fields['endereco'].label = mark_safe(' <i class="fas fa-building"></i> endereco')
        self.fields['localizacao'].label = mark_safe(' <i class="fas fa-globe"></i> localizacao')
        self.fields['historico_interacoes'].label = mark_safe(' <i class="fas fa-comments"></i> historico_interacoes')
        self.fields['historico_compras'].label = mark_safe(' <i class="fas fa-shopping-cart"></i> historico_compras')
        self.fields['fonte_aquisicao'].label = mark_safe(' <i class="fas fa-globe"></i> fonte_aquisicao')
        self.fields['campanhas_marketing'].label = mark_safe(' <i class="fas fa-bullhorn"></i> campanhas_marketing')
        self.fields['tarefas'].label = mark_safe(' <i class="fas fa-tasks"></i> tarefas')
        self.fields['interesses'].label = mark_safe(' <i class="fas fa-heart"></i> interesses')
        self.fields['historico_suporte'].label = mark_safe(' <i class="fas fa-life-ring"></i> historico_suporte')
        self.fields['tags'].label = mark_safe(' <i class="fas fa-tags"></i> tags')
        self.fields['perfil_social'].label = mark_safe(' <i class="fas fa-link"></i> perfil_social')


        # Adicione as classes de estilo para os campos
        for field_name in self.fields:
            self.fields[field_name].widget.attrs['class'] = 'form-control'







