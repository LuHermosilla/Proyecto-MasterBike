# Generated by Django 5.0.6 on 2024-07-16 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_tipo_user_alter_user_numrut_alter_user_telefono_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id_tipo',
            field=models.IntegerField(null=True),
        ),
    ]
