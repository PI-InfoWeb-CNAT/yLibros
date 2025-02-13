# Generated by Django 5.1.3 on 2025-01-17 12:28

import validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("elibrosLoja", "0020_remove_historicalpedido_qtd_vendidos_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="historicallivro",
            name="ano_de_publicacao",
            field=models.IntegerField(
                blank=True,
                null=True,
                validators=[
                    validators.nao_negativo,
                    validators.nao_nulo,
                    validators.nao_e_no_futuro,
                ],
                verbose_name="Ano de Publicação",
            ),
        ),
        migrations.AlterField(
            model_name="historicallivro",
            name="data_de_publicacao",
            field=models.DateField(
                blank=True,
                null=True,
                validators=[validators.nao_e_no_futuro],
                verbose_name="Data de Publicação",
            ),
        ),
        migrations.AlterField(
            model_name="historicallivro",
            name="desconto",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                max_digits=5,
                null=True,
                verbose_name="Desconto",
            ),
        ),
        migrations.AlterField(
            model_name="historicallivro",
            name="editora",
            field=models.CharField(
                default="Editora não informada", max_length=100, verbose_name="Editora"
            ),
        ),
        migrations.AlterField(
            model_name="historicallivro",
            name="preco",
            field=models.DecimalField(
                decimal_places=2,
                default=0.0,
                max_digits=5,
                validators=[validators.nao_negativo, validators.nao_nulo],
                verbose_name="Preço",
            ),
        ),
        migrations.AlterField(
            model_name="historicallivro",
            name="quantidade",
            field=models.IntegerField(
                validators=[validators.nao_negativo], verbose_name="Quantidade"
            ),
        ),
        migrations.AlterField(
            model_name="historicallivro",
            name="sinopse",
            field=models.TextField(blank=True, null=True, verbose_name="Sinopse"),
        ),
        migrations.AlterField(
            model_name="historicallivro",
            name="subtitulo",
            field=models.CharField(
                blank=True, max_length=200, null=True, verbose_name="Subtítulo"
            ),
        ),
        migrations.AlterField(
            model_name="historicallivro",
            name="titulo",
            field=models.CharField(max_length=200, verbose_name="Título"),
        ),
        migrations.AlterField(
            model_name="historicalpedido",
            name="numero_pedido",
            field=models.CharField(
                db_index=True, default="837847360921", max_length=12
            ),
        ),
        migrations.AlterField(
            model_name="historicalpedido",
            name="status",
            field=models.CharField(
                default="PRO", max_length=50, validators=[validators.nao_nulo]
            ),
        ),
        migrations.AlterField(
            model_name="livro",
            name="ano_de_publicacao",
            field=models.IntegerField(
                blank=True,
                null=True,
                validators=[
                    validators.nao_negativo,
                    validators.nao_nulo,
                    validators.nao_e_no_futuro,
                ],
                verbose_name="Ano de Publicação",
            ),
        ),
        migrations.AlterField(
            model_name="livro",
            name="autor",
            field=models.ManyToManyField(
                blank=True,
                related_name="Autor_do_Livro",
                to="elibrosLoja.autor",
                verbose_name="Autor(es)",
            ),
        ),
        migrations.AlterField(
            model_name="livro",
            name="data_de_publicacao",
            field=models.DateField(
                blank=True,
                null=True,
                validators=[validators.nao_e_no_futuro],
                verbose_name="Data de Publicação",
            ),
        ),
        migrations.AlterField(
            model_name="livro",
            name="desconto",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                max_digits=5,
                null=True,
                verbose_name="Desconto",
            ),
        ),
        migrations.AlterField(
            model_name="livro",
            name="editora",
            field=models.CharField(
                default="Editora não informada", max_length=100, verbose_name="Editora"
            ),
        ),
        migrations.AlterField(
            model_name="livro",
            name="preco",
            field=models.DecimalField(
                decimal_places=2,
                default=0.0,
                max_digits=5,
                validators=[validators.nao_negativo, validators.nao_nulo],
                verbose_name="Preço",
            ),
        ),
        migrations.AlterField(
            model_name="livro",
            name="quantidade",
            field=models.IntegerField(
                validators=[validators.nao_negativo], verbose_name="Quantidade"
            ),
        ),
        migrations.AlterField(
            model_name="livro",
            name="sinopse",
            field=models.TextField(blank=True, null=True, verbose_name="Sinopse"),
        ),
        migrations.AlterField(
            model_name="livro",
            name="subtitulo",
            field=models.CharField(
                blank=True, max_length=200, null=True, verbose_name="Subtítulo"
            ),
        ),
        migrations.AlterField(
            model_name="livro",
            name="titulo",
            field=models.CharField(max_length=200, verbose_name="Título"),
        ),
        migrations.AlterField(
            model_name="pedido",
            name="numero_pedido",
            field=models.CharField(
                default="837847360921", max_length=12, primary_key=True, serialize=False
            ),
        ),
        migrations.AlterField(
            model_name="pedido",
            name="status",
            field=models.CharField(
                default="PRO", max_length=50, validators=[validators.nao_nulo]
            ),
        ),
    ]
