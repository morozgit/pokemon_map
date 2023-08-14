from django.db import models  # noqa F401


class Pokemon(models.Model):
    title_ru = models.CharField(max_length=200)
    title_en = models.CharField(max_length=200, blank=True)
    title_jp = models.CharField(max_length=200, blank=True)
    describe = models.TextField(blank=True)
    photo = models.ImageField(upload_to='pokemon')
    previous_evolution = models.ForeignKey('self',
                                           verbose_name='Из кого эволюционирует',
                                           null=True,
                                           blank=True,
                                           related_name='next_evolutions',
                                           on_delete=models.SET_NULL)

    def __str__(self) -> str:
        return self.title_ru


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon,
                                on_delete=models.CASCADE,
                                related_name="entities")
    latitude = models.FloatField(verbose_name='Широта')
    longitude = models.FloatField(verbose_name='Долгота')
    appeared_at = models.DateTimeField(verbose_name='Появится в')
    disappeared_at = models.DateTimeField(verbose_name='Исчезнет в')
    level = models.IntegerField(null=True, blank=True,
                                verbose_name='Уровень')
    heath = models.IntegerField(null=True, blank=True,
                                verbose_name='Здоровье')
    strength = models.IntegerField(null=True, blank=True,
                                   verbose_name='Сила')
    defense = models.IntegerField(null=True, blank=True,
                                  verbose_name='Защита')
    stamina = models.IntegerField(null=True, blank=True,
                                  verbose_name='Выносливость')

    def __str__(self) -> str:
        return self.pokemon.title_ru
