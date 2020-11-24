# Generated by Django 3.0.6 on 2020-07-12 21:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Albuns',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100, verbose_name='titulo')),
                ('data', models.DateField(verbose_name='data')),
            ],
            options={
                'verbose_name': 'Album',
                'verbose_name_plural': 'Albuns',
                'ordering': ['titulo'],
            },
        ),
        migrations.CreateModel(
            name='Bandas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='nome')),
            ],
            options={
                'verbose_name': 'Banda',
                'verbose_name_plural': 'Bandas',
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='Musicas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100, verbose_name='titulo')),
                ('segundos', models.IntegerField(default=0, verbose_name='segundos')),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='disco.Albuns')),
            ],
            options={
                'verbose_name': 'Musica',
                'verbose_name_plural': 'Musicas',
                'ordering': ['titulo'],
            },
        ),
        migrations.AddField(
            model_name='albuns',
            name='banda',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='disco.Bandas'),
        ),
    ]
