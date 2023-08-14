from django.db import models  # noqa F401


class Pokemon(models.Model):
    title_ru = models.CharField(max_length=200)
    title_en = models.CharField(max_length=200)
    title_jp = models.CharField(max_length=200)
    describe = models.TextField(max_length=1000)
    photo = models.ImageField(upload_to='pokemon', null=True)
    previous_evolution = models.ForeignKey('self',
                                           verbose_name='Из кого эволюционирует',
                                           null=True,
                                           blank=True,
                                           related_name='next_evolutions',
                                           on_delete=models.SET_NULL)

    def __str__(self) -> str:
        return "{}".format(self.title_ru)


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, related_name="entities",)
    latitude = models.FloatField()
    longitude = models.FloatField()
    appeared_at = models.DateTimeField()
    disappeared_at = models.DateTimeField()
    level = models.IntegerField(default=0)
    heath = models.IntegerField(default=100)
    strength = models.IntegerField(default=0)
    defense = models.IntegerField(default=0)
    stamina = models.IntegerField(default=0)
