from django.db import models  # noqa F401


class Pokemon(models.Model):
    title_ru = models.CharField(max_length=200, default='')
    title_en = models.CharField(max_length=200, default='', blank=True)
    title_jp = models.CharField(max_length=200, default='', blank=True)
    describe = models.TextField(max_length=1000, default='', blank=True)
    photo = models.ImageField(upload_to='pokemon', null=False, blank=False)
    previous_evolution = models.ForeignKey('self',
                                           verbose_name='Из кого эволюционирует',
                                           null=True,
                                           blank=True,
                                           related_name='next_evolutions',
                                           on_delete=models.SET_NULL)

    def __str__(self) -> str:
        return "{}".format(self.title_ru)


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon,
                                on_delete=models.CASCADE,
                                related_name="entities",
                                null=False, blank=False)
    latitude = models.FloatField(null=False, blank=False)
    longitude = models.FloatField(null=False, blank=False)
    appeared_at = models.DateTimeField(null=False, blank=False)
    disappeared_at = models.DateTimeField(null=False, blank=False)
    level = models.IntegerField(default=0, null=True, blank=True)
    heath = models.IntegerField(default=100, null=True, blank=True)
    strength = models.IntegerField(default=0, null=True, blank=True)
    defense = models.IntegerField(default=0, null=True, blank=True)
    stamina = models.IntegerField(default=0, null=True, blank=True)
