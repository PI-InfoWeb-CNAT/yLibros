# Generated by Django 5.1.3 on 2025-01-20 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("elibrosLoja", "0022_alter_autor_options_alter_categoria_options_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="historicalpedido",
            name="numero_pedido",
            field=models.CharField(
                db_index=True, default="399673201492", max_length=12
            ),
        ),
        migrations.AlterField(
            model_name="pedido",
            name="numero_pedido",
            field=models.CharField(
                default="399673201492", max_length=12, primary_key=True, serialize=False
            ),
        ),
    ]
