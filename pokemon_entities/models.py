from django.db import models  # noqa F401

# your models here
class Pokemon(models.Model):
    """Покемон"""
    evolution = models.ForeignKey('self', verbose_name='В кого эволюционирует',
                                  related_name="evolutions", on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(verbose_name='Название', max_length=200)
    title_en = models.CharField(verbose_name='Название на английском', max_length=200, null=True, blank=True)
    title_jp = models.CharField(verbose_name='Название на японском', max_length=200, null=True, blank=True)
    image = models.ImageField(verbose_name='Адрес картинки', upload_to='pokemon', null=True, blank=True)
    description = models.TextField(verbose_name='Описание покемона', null=True, blank=True)

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    """Сущности покемона"""
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    lat = models.FloatField(verbose_name='Координаты: широта', null=True, blank=True)
    lon = models.FloatField(verbose_name='Координаты: долгота', null=True, blank=True)
    appeared_at = models.DateTimeField(verbose_name='Дата появления на карте', null=True, blank=True)
    disappeared_at = models.DateTimeField(verbose_name='Дата исчезновения на карте', null=True, blank=True)
    level = models.IntegerField(verbose_name='Уровень покемона', null=True, blank=True)
    health = models.IntegerField(verbose_name='Здоровье', null=True, blank=True)
    strength = models.IntegerField(verbose_name='Сила', null=True, blank=True)
    defence = models.IntegerField(verbose_name='Защита', null=True, blank=True)
    stamina = models.IntegerField(verbose_name='Выносливость', null=True, blank=True)

    def __str__(self):
        return f'{self.pokemon},{self.lat},{self.lon}'
