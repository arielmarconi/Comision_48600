# Generated by Django 4.1 on 2023-03-29 22:32

import Staff.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Staff', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OtrosEmpleados',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            bases=(models.Model, Staff.models.Persona),
        ),
    ]
