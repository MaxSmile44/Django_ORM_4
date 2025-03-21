# Generated by Django 3.1.14 on 2025-03-21 11:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0017_auto_20250321_1410'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pokemon',
            name='evolution',
        ),
        migrations.AddField(
            model_name='pokemon',
            name='change',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='changes', to='pokemon_entities.pokemon', verbose_name='В кого эволюционирует'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='pokemon',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entities', to='pokemon_entities.pokemon', verbose_name='Покемон'),
        ),
    ]
