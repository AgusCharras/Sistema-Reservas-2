# Generated by Django 4.2.3 on 2023-07-04 23:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0010_alter_cabania_complejo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cabania',
            name='complejo',
            field=models.ForeignKey(default='none', on_delete=django.db.models.deletion.CASCADE, to='reservas.complejo'),
        ),
    ]
