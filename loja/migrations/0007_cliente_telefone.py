# Generated by Django 5.0.4 on 2024-06-03 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0006_cliente_pedido_itenspedido'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='telefone',
            field=models.CharField(max_length=50, null=True),
        ),
    ]