# Generated by Django 3.1.14 on 2025-03-18 10:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0006_auto_20250318_1353'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pokemon',
            old_name='show_pokemon',
            new_name='description',
        ),
    ]
