# Generated by Django 4.2.3 on 2023-07-04 23:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0011_alter_cabania_complejo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reserva',
            name='servicios',
        ),
        migrations.AddField(
            model_name='reserva',
            name='servicios',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='reservas.servicio'),
        ),
    ]
