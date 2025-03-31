# Generated by Django 3.1.14 on 2025-03-31 08:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0018_auto_20250321_1440'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pokemon',
            name='change',
        ),
        migrations.AddField(
            model_name='pokemon',
            name='next_evolution',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='previous_evolution', to='pokemon_entities.pokemon', verbose_name='В кого эволюционирует'),
        ),
    ]
