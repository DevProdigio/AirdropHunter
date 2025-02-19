# Generated by Django 5.1.2 on 2025-02-14 21:38

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airdrop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='airdrop',
            name='data_publicacao',
            field=models.DateField(default=django.utils.timezone.now, null=True),
        ),
        migrations.AddField(
            model_name='airdrop',
            name='plataforma',
            field=models.CharField(choices=[('BLOCKCHAIN', 'Blockchain'), ('TELEGRAM', 'Telegram'), ('GAMES', 'Games')], max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='airdrop',
            name='investimento',
            field=models.CharField(choices=[('FREE', 'Free'), ('OPCIONAL', 'Opção de Investimento'), ('PAGO', 'Pago')], max_length=14),
        ),
        migrations.AlterField(
            model_name='airdrop',
            name='status',
            field=models.CharField(choices=[('ACONTECENDO', 'Acontecendo'), ('SAQUE LIBERADO', 'Saque Liberado')], max_length=20),
        ),
    ]
