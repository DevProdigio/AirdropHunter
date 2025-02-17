from django import forms
from .models import Airdrop

class IndiqueAirdropForm(forms.Form):
    # Campo nome
    nome = forms.CharField(
        label='Nome',
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Seu nome'})
    )

    # Campo e-mail
    email = forms.EmailField(  # Use EmailField para validar e-mails corretamente
        label='E-mail',
        widget=forms.EmailInput(attrs={'placeholder': 'Seu E-mail'})
    )

    # Campo plataforma (usando ChoiceField)
    plataforma = forms.ChoiceField(
        label="Plataforma do projeto",
        choices=[
            ('BLOCKCHAIN', 'Blockchain'),
            ('TELEGRAM', 'Telegram'),
            ('GAMES', 'Games'),
        ],
        widget=forms.Select(attrs={'class': 'form-control'})  # Widget personalizado
    )

    # Campo investimento (usando ChoiceField)
    investimento = forms.ChoiceField(
        label="Tipo de investimento",
        choices=[
            ('FREE', 'Free'),
            ('OPCIONAL', 'Opcional'),
            ('PAGO', 'Pago'),
        ],
        widget=forms.Select(attrs={'class': 'form-control'})  # Widget personalizado
    )

    # Campo link
    link = forms.URLField(
        label="Link do projeto",
        widget=forms.URLInput(attrs={'placeholder': 'Link do projeto'})  # Corrigido para URLInput
    )