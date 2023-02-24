# Generated by Django 4.1 on 2023-02-06 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deliveries', '0006_alter_deliveries_payment_method'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deliveries',
            name='payment_method',
            field=models.CharField(choices=[('Efectivo', 'Efectivo'), ('Tarjeta', 'Tarjeta'), ('Transferencia', 'Transferencia')], max_length=13),
        ),
    ]