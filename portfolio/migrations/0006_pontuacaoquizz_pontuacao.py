# Generated by Django 4.0.4 on 2022-05-27 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_colega_pontuacaoquizz_professor_projeto_cadeira_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pontuacaoquizz',
            name='pontuacao',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
