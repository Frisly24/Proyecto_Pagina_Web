# Generated by Django 4.0.3 on 2022-10-04 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0005_employee_date_joined'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='date_creation',
            field=models.DateTimeField(auto_now=True),
        ),
    ]