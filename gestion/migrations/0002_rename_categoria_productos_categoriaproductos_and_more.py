# Generated by Django 5.0.6 on 2024-06-11 23:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Categoria_Productos',
            new_name='CategoriaProductos',
        ),
        migrations.RenameModel(
            old_name='Estado_Envios',
            new_name='EstadoEnvios',
        ),
        migrations.RenameModel(
            old_name='Formas_Pago',
            new_name='EstadosArriendo',
        ),
        migrations.RenameModel(
            old_name='Estados_Pedido',
            new_name='EstadosPedido',
        ),
        migrations.RenameModel(
            old_name='Estados_Reparacion',
            new_name='EstadosReparacion',
        ),
        migrations.RenameModel(
            old_name='Historial_Mantenciones',
            new_name='HistorialMantenciones',
        ),
        migrations.RenameModel(
            old_name='Informes_Gestion',
            new_name='InformesGestion',
        ),
        migrations.RenameModel(
            old_name='Tipo_Promocion',
            new_name='TipoPromocion',
        ),
        migrations.RenameModel(
            old_name='Trazabilidad_Envios',
            new_name='TrazabilidadEnvios',
        ),
        migrations.RenameField(
            model_name='estadosarriendo',
            old_name='forma_pago',
            new_name='estado_arriendo',
        ),
        migrations.RenameField(
            model_name='estadosarriendo',
            old_name='id_forma_pago',
            new_name='id_estado_arriendo',
        ),
        migrations.AddField(
            model_name='arriendos',
            name='estado_arriendo',
            field=models.ForeignKey(db_column='id_estado_arriendo', default=1, on_delete=django.db.models.deletion.CASCADE, to='gestion.estadosarriendo'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='arriendos',
            name='forma_pago',
            field=models.CharField(max_length=20),
        ),
    ]
