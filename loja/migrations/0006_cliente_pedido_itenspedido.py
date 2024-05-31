# Generated by Django 5.0.6 on 2024-05-31 21:43

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0005_alter_produto_imagem'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, null=True)),
                ('email', models.CharField(max_length=100)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_Pedido', models.DateTimeField(auto_now_add=True)),
                ('completo', models.BooleanField(max_length=100, null=True)),
                ('cliente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='loja.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='ItensPedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField(blank=True, default=0, null=True)),
                ('dataAdicionado', models.DateTimeField(auto_now_add=True)),
                ('produto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='loja.produto')),
                ('pedido', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='loja.pedido')),
            ],
        ),
    ]
