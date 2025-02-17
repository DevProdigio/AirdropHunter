from django.contrib import admin
from .models import Airdrop

# Alterar o título no topo da página admin
admin.site.site_header = "Painel Administrativo Hunter"

# Alterar o título exibido na aba do navegador
admin.site.site_title = "Administração Hunter"

# Alterar o texto exibido na página inicial do admin
admin.site.index_title = "Bem-vindo ao painel administrativo Hunter"

admin.site.register(Airdrop)


