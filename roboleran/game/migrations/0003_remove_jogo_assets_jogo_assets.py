# Generated by Django 5.1.2 on 2024-11-07 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0002_remove_asset_nome_alter_asset_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jogo',
            name='assets',
        ),
        migrations.AddField(
            model_name='jogo',
            name='assets',
            field=models.ManyToManyField(to='game.asset'),
        ),
    ]
