# Generated by Django 4.0.3 on 2022-10-04 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0008_employee_salary'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='state',
            field=models.BooleanField(default=True),
        ),
    ]