# Generated by Django 5.0.6 on 2024-06-03 19:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0003_logentry_add_action_flag_choices'),
        ('auth', '0012_alter_user_first_name_max_length'),
        ('loja', '0009_alter_cliente_options_remove_cliente_email_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CustomUser',
            new_name='MudandoUser',
        ),
    ]
