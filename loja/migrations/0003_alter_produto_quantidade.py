# Generated by Django 5.0.6 on 2024-05-31 11:13

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0002_produto_quantidade_alter_produto_tipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='quantidade',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]
