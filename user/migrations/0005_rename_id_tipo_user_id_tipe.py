# Generated by Django 5.0.6 on 2024-07-16 15:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_alter_user_id_tipo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='id_tipo',
            new_name='id_tipe',
        ),
    ]
