# Generated by Django 5.0 on 2023-12-12 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('apellidos', models.CharField(max_length=40)),
                ('correo', models.EmailField(max_length=254)),
                ('telefono', models.CharField(max_length=9)),
            ],
            options={
                'ordering': ['nombre', 'apellidos'],
            },
        ),
        migrations.AlterField(
            model_name='piso',
            name='fechaAlta',
            field=models.DateField(auto_now_add=True, verbose_name='Fecha de alta'),
        ),
        migrations.AlterField(
            model_name='piso',
            name='fechaModificacion',
            field=models.DateField(auto_now=True, verbose_name='Fecha de modificación'),
        ),
    ]
