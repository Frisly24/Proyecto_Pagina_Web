# Generated by Django 4.0.3 on 2022-10-09 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0012_client_detsale_product_sale_size_delete_employee_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='tall',
        ),
        migrations.AddField(
            model_name='product',
            name='color',
            field=models.CharField(choices=[('Negro', 'Negro'), ('Gris', 'Gris'), ('Blanco', 'Blanco')], default='Negro', max_length=10, verbose_name='Color'),
        ),
        migrations.AddField(
            model_name='product',
            name='talla',
            field=models.CharField(choices=[('6', '6-S'), ('6.5', '6.5-S'), ('7', '7-S'), ('7.5', '7.5-S'), ('8', '8-S'), ('8.5', '8.5-M'), ('9', '9-M'), ('9.5', '9.5-L'), ('10', '10-L'), ('10.5', '10.5-L'), ('11', '11-XL'), ('11.5', '11.5-XL'), ('12', '12-XL')], default='10', max_length=10, verbose_name='Talla'),
        ),
        migrations.DeleteModel(
            name='size',
        ),
    ]
