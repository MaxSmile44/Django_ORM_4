import folium

from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from pogomap.settings import MEDIA_URL
from pokemon_entities.models import Pokemon

MOSCOW_CENTER = [55.751244, 37.618423]
DEFAULT_IMAGE_URL = (
    'https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision'
    '/latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832'
    '&fill=transparent'
)


def add_pokemon(folium_map, lat, lon, image_url=DEFAULT_IMAGE_URL):
    icon = folium.features.CustomIcon(
        image_url,
        icon_size=(50, 50),
    )
    folium.Marker(
        [lat, lon],
        # Warning! `tooltip` attribute is disabled intentionally
        # to fix strange folium cyrillic encoding bug
        icon=icon,
    ).add_to(folium_map)


def create_map(request, pokemon, folium_map):
    for entity in pokemon.entities.all():
        if entity.appeared_at:
            if (timezone.localtime() > entity.appeared_at.astimezone()
                    and (not entity.disappeared_at
                         or timezone.localtime() < entity.disappeared_at.astimezone())):
                add_pokemon(
                    folium_map,
                    entity.lat,
                    entity.lon,
                    request.build_absolute_uri(f'{MEDIA_URL}{pokemon.image}')
                )


def show_all_pokemons(request):
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    pokemons = Pokemon.objects.all()
    pokemons_on_page = []
    for pokemon in pokemons:
        create_map(request, pokemon, folium_map)
        pokemons_on_page.append({
            'pokemon_id': pokemon.pk,
            'img_url': request.build_absolute_uri(f'{MEDIA_URL}{pokemon.image}'),
            'title_ru': pokemon.title,
        })

    return render(request, 'mainpage.html', context={
        'map': folium_map._repr_html_(),
        'pokemons': pokemons_on_page,
    })


def show_pokemon(request, pokemon_id):
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    pokemon = get_object_or_404(Pokemon, pk=pokemon_id)
    pokemon_on_page = {
        'pokemon_id': pokemon.pk,
        'img_url': request.build_absolute_uri(pokemon.image.url),
        'title_ru': pokemon.title,
        'title_en': pokemon.title_en,
        'title_jp': pokemon.title_jp,
        'description': pokemon.description,
    }
    if pokemon.changes.first():
        pokemon_on_page['previous_evolution'] = {
                'title_ru': pokemon.changes.first().title,
                'pokemon_id': pokemon.changes.first().pk,
                'img_url': request.build_absolute_uri(pokemon.changes.first().image.url),
        }
    if pokemon.change:
        pokemon_on_page['next_evolution'] = {
                'title_ru': pokemon.change.title,
                'pokemon_id': pokemon.change.pk,
                'img_url': request.build_absolute_uri(pokemon.change.image.url),
        }

    create_map(request, pokemon, folium_map)

    return render(request, 'pokemon.html', context={
        'map': folium_map._repr_html_(),
        'pokemon': pokemon_on_page,
    })
