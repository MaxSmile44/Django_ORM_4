# Generated by Django 3.1.14 on 2025-03-21 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0014_auto_20250321_1344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemonentity',
            name='defence',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Защита'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='health',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Здоровье'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='level',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Уровень покемона'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='stamina',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Выносливость'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='strength',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Сила'),
        ),
    ]
