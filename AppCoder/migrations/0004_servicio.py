# Generated by Django 4.0.1 on 2022-03-27 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0003_clientes_delete_reservas'),
    ]

    operations = [
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('servicio', models.CharField(max_length=40)),
                ('precio', models.IntegerField()),
            ],
        ),
    ]