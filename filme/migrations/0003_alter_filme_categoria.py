# Generated by Django 4.0.4 on 2022-08-09 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filme', '0002_rename_credcricao_filme_descricao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filme',
            name='categoria',
            field=models.CharField(choices=[('ANALISE', 'Análise'), ('PROGRAMACAO', 'Programação'), ('APRESENTACAO', 'Apresentação'), ('OUTROS', 'outros')], max_length=15),
        ),
    ]
