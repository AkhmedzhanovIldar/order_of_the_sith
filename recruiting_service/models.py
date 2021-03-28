from django.db import models


class Planet(models.Model):
    """Планета"""
    name = models.CharField(max_length=255, verbose_name='Наименование')

    class Meta:
        verbose_name = 'Планета'
        verbose_name_plural = 'Планеты'

    def __str__(self):
        return self.name


class Sith(models.Model):
    """Ситх"""
    name = models.CharField(max_length=255, verbose_name='Имя')
    planet = models.ForeignKey(
        to='Planet', verbose_name='Планета обучения', on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Ситх'
        verbose_name_plural = 'Ситхи'

    def __str__(self):
        return 'Имя: {name}, Планета: {planet}.'.format(name=self.name, planet=self.planet)


class Recruit(models.Model):
    """Рекрут"""
    name = models.CharField(max_length=255, verbose_name='Имя')
    planet = models.ForeignKey(
        to='Planet', verbose_name='Планета обитания', on_delete=models.PROTECT)
    age = models.IntegerField(verbose_name='Возрас')
    email = models.EmailField(verbose_name='Email')

    class Meta:
        verbose_name = 'Рекрут'
        verbose_name_plural = 'Рекруты'

    def __str__(self):
        return 'Имя: {name}, Планета: {planet}, Возраст: {age}, Email: {email}'.format(name=self.name, planet=self.planet, age=self.age, email=self.email)


class ShadowHand(models.Model):
    """Рекруты зачисленные ситхом Рукой Тени"""
    recruit = models.ForeignKey(to='Recruit', verbose_name='Рекрут', on_delete=models.PROTECT)
    sith = models.ForeignKey(to='Sith', verbose_name='Ситх', on_delete = models.PROTECT)

    class Meta:
        verbose_name = 'Рука Тени'
        verbose_name_plural = 'Руки Тени'

    def __str__(self):
        return 'Рекрут: {recruit}, Ситх: {sith}'.format(recruit=self.recruit, sith=self.sith)
