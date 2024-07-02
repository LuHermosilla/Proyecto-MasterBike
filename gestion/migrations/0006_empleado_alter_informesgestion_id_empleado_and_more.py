# Generated by Django 5.0.6 on 2024-06-30 01:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0005_rename_cargo_emp_empleados_id_cargo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id_empleado', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre_emp', models.CharField(max_length=20)),
                ('aPaterno_emp', models.CharField(max_length=20)),
                ('aMaterno_emp', models.CharField(max_length=20)),
                ('rut_emp', models.IntegerField(max_length=8, unique=True)),
                ('dv', models.IntegerField(max_length=1)),
                ('id_cargo', models.ForeignKey(db_column='id_cargo', on_delete=django.db.models.deletion.CASCADE, to='gestion.cargos')),
                ('id_sucursal', models.ForeignKey(db_column='id_sucursal', on_delete=django.db.models.deletion.CASCADE, to='gestion.sucursales')),
            ],
        ),
        migrations.AlterField(
            model_name='informesgestion',
            name='id_empleado',
            field=models.ForeignKey(db_column='id_empleado', on_delete=django.db.models.deletion.CASCADE, to='gestion.empleado'),
        ),
        migrations.AlterField(
            model_name='pedidos',
            name='id_empleado',
            field=models.ForeignKey(db_column='id_empleado', on_delete=django.db.models.deletion.CASCADE, to='gestion.empleado'),
        ),
        migrations.AlterField(
            model_name='reparaciones',
            name='id_empleado',
            field=models.ForeignKey(db_column='id_empleado', on_delete=django.db.models.deletion.CASCADE, to='gestion.empleado'),
        ),
        migrations.DeleteModel(
            name='Empleados',
        ),
    ]
