# Generated by Django 4.0.1 on 2022-03-30 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0007_alter_juego_imagen'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='servicio',
            options={'verbose_name': 'servicio', 'verbose_name_plural': 'servicios'},
        ),
        migrations.AlterField(
            model_name='juego',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='juegos'),
        ),
    ]