# Generated by Django 3.1.14 on 2025-03-18 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0005_pokemonentity_show_pokemon'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pokemonentity',
            name='show_pokemon',
        ),
        migrations.AddField(
            model_name='pokemon',
            name='show_pokemon',
            field=models.TextField(blank=True, null=True),
        ),
    ]
