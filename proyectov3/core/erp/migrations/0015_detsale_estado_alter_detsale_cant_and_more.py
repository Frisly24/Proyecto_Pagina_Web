# Generated by Django 4.0.3 on 2022-10-10 00:45

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0014_alter_client_cui'),
    ]

    operations = [
        migrations.AddField(
            model_name='detsale',
            name='estado',
            field=models.CharField(choices=[('En Bodega', 'En Bodega'), ('En Ruta', 'En Ruta'), ('Entregado', 'Entregado')], default='En Bodega', max_length=15, verbose_name='Estado'),
        ),
        migrations.AlterField(
            model_name='detsale',
            name='cant',
            field=models.IntegerField(default=0, verbose_name='Cantidad'),
        ),
        migrations.AlterField(
            model_name='detsale',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=9, verbose_name='Precio'),
        ),
        migrations.AlterField(
            model_name='detsale',
            name='prod',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erp.product', verbose_name='Producto'),
        ),
        migrations.AlterField(
            model_name='detsale',
            name='sale',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erp.sale', verbose_name='Venta'),
        ),
        migrations.AlterField(
            model_name='detsale',
            name='subtotal',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=9, verbose_name='Total'),
        ),
        migrations.AlterField(
            model_name='sale',
            name='cli',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erp.client', verbose_name='Cliente'),
        ),
        migrations.AlterField(
            model_name='sale',
            name='date_joined',
            field=models.DateField(default=datetime.datetime.now, verbose_name='Fecha de la Venta'),
        ),
        migrations.AlterField(
            model_name='sale',
            name='iva',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=9, verbose_name='IVA'),
        ),
        migrations.AlterField(
            model_name='sale',
            name='subtotal',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=9, verbose_name='Subtotal'),
        ),
        migrations.AlterField(
            model_name='sale',
            name='total',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=9, verbose_name='Total'),
        ),
    ]
