# Generated by Django 3.0.7 on 2020-10-09 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodcartapp', '0037_auto_20201009_1704'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='payment_method',
            field=models.CharField(choices=[('Cash', 'Наличными'), ('By card', 'Картой')], default='Cash', max_length=11, verbose_name='Способ оплаты'),
        ),
    ]
