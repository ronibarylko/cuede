# Generated by Django 2.2.2 on 2019-12-31 00:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('enunciados', '0017_version_texto_superclase'),
    ]

    operations = [
        migrations.CreateModel(
            name='Voto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('positivo', models.BooleanField()),
                ('posteo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enunciados.Posteo')),
            ],
        ),
        migrations.RemoveField(
            model_name='informacionusuario',
            name='votos_enunciados',
        ),
        migrations.DeleteModel(
            name='VotoEnunciado',
        ),
        migrations.AddField(
            model_name='voto',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enunciados.InformacionUsuario'),
        ),
        migrations.AddField(
            model_name='informacionusuario',
            name='votos',
            field=models.ManyToManyField(through='enunciados.Voto', to='enunciados.Posteo'),
        ),
    ]