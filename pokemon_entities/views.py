import folium
import json

from django.http import HttpResponseNotFound
from django.shortcuts import render
from .models import Pokemon, PokemonEntity
from django.utils.timezone import localtime
from django.shortcuts import get_object_or_404

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


def show_all_pokemons(request):
    time = localtime()
    active_pokemons = PokemonEntity.objects.filter(appeared_at__lte=time,
                                                  disappeared_at__gte=time)
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for pokemon in active_pokemons:
        pokemon_url = request.build_absolute_uri(pokemon.pokemon.photo.url)
        add_pokemon(
            folium_map, pokemon.latitude,
            pokemon.longitude,
            pokemon_url
        )

    pokemons_on_page = []
    for pokemon in Pokemon.objects.all():
        pokemons_on_page.append({
            'pokemon_id': pokemon.id,
            'img_url': pokemon.photo.url,
            'title_ru': pokemon.title_ru,
            'title_en': pokemon.title_ru,
            'title_jp': pokemon.title_ru,
        })

    return render(request, 'mainpage.html', context={
        'map': folium_map._repr_html_(),
        'pokemons': pokemons_on_page,
    })


def show_pokemon(request, pokemon_id):
    requested_pokemon = get_object_or_404(Pokemon, id=int(pokemon_id))
    pokemon_url = request.build_absolute_uri(requested_pokemon.photo.url)
    pokemon = {
        'pokemon_id': requested_pokemon.id,
        'title_ru': requested_pokemon.title_ru,
        'title_en': requested_pokemon.title_en,
        'title_jp': requested_pokemon.title_jp,
        'description': requested_pokemon.describe,
        'img_url': pokemon_url
    }

    time = localtime()
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    active_pokemons = requested_pokemon.entities.filter(appeared_at__lte=time,
                                                        disappeared_at__gte=time)
    for entity_pokemon in active_pokemons:
        add_pokemon(
            folium_map, entity_pokemon.latitude,
            requested_pokemon.longitude,
            pokemon_url
        )

    return render(request, 'pokemon.html', context={
        'map': folium_map._repr_html_(), 'pokemon': pokemon
    })
