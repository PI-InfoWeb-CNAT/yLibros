# Generated by Django 5.1.3 on 2024-11-24 22:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("elibrosLoja", "0002_alter_livro_data_de_adicao_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="livro",
            name="data_de_adicao",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 11, 24, 19, 54, 51, 714712)
            ),
        ),
        migrations.AlterField(
            model_name="pedido",
            name="data_de_pedido",
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name="pedido",
            name="numero_pedido",
            field=models.CharField(
                default="535331227776", max_length=12, primary_key=True, serialize=False
            ),
        ),
    ]
