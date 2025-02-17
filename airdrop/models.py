from django.db import models
from django.utils import timezone



class Airdrop(models.Model):


    PLATAFORMA_CHOICES = [
        ('BLOCKCHAIN', 'Blockchain'),
        ('TELEGRAM', 'Telegram'),
        ('GAMES', 'Games'),
    ]

    STATUS_CHOICES = [
        ('ACONTECENDO', 'Acontecendo'),
        ('SAQUE LIBERADO', 'Saque Liberado'),
    ]
    INVESTIMENTO_CHOICES = [
        ('FREE', 'Free'),
        ('OPCIONAL', 'Opção de Investimento'),
        ('PAGO', 'Pago'),
    ]

    nome = models.CharField(max_length=255)
    plataforma = models.CharField(null=True, max_length=40, choices=PLATAFORMA_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    data_publicacao = models.DateField(null=True, default=timezone.now)
    data_encerramento = models.DateField(null=True, blank=True)
    investimento = models.CharField(max_length=14, choices=INVESTIMENTO_CHOICES)
    valor_investimento = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    url = models.URLField()
    
    def __str__(self):
        return self.nome