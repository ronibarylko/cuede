# Generated by Django 2.2.2 on 2020-01-09 16:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('enunciados', '0022_solucion_creador'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='voto',
            unique_together={('usuario', 'solucion')},
        ),
    ]