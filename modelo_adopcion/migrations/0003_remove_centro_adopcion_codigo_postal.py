# Generated by Django 5.0.1 on 2024-02-12 23:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('modelo_adopcion', '0002_remove_mascota_edad_alter_mascota_nombre'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='centro_adopcion',
            name='codigo_postal',
        ),
    ]
