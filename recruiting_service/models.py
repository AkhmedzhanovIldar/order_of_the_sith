from django.db import models

class Planet(models.Model):
    name = models.CharField(max_length=150, verbose_name='Наименование')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Планета'
        verbose_name_plural = 'Планеты'

class Recruit(models.Model):
    name = models.CharField(max_length=150, verbose_name='Имя')
    planet = models.ForeignKey(Planet, verbose_name='Планета', on_delete=models.PROTECT)
    age = models.IntegerField(verbose_name='Возраст')
    email = models.EmailField(max_length=200, verbose_name='Email')

    def __str__(self):
        return 'Имя: %s, Планета: %s, Возраст: %s, Email: %s' % (self.name, self.planet, self.age, self.email)

    class Meta:
        verbose_name = 'Рекрут'
        verbose_name_plural = 'Рекруты'

class Sith(models.Model):
    name = models.CharField(max_length=150, verbose_name='Имя')
    planet = models.ForeignKey(Planet, verbose_name='Планета', on_delete=models.PROTECT)

    def __str__(self):
        return '%s, %s' % (self.name, self.planet)
    
    class Meta:
        verbose_name = 'Ситх'
        verbose_name_plural = 'Ситхи'

class ShadowHand(models.Model):
    recruit = models.ForeignKey(Recruit, verbose_name='Рекрут', on_delete=models.PROTECT)
    sith = models.ForeignKey(Sith, verbose_name='Ситх', on_delete = models.PROTECT)

    def __str__(self):
        return 'Рекрут: %s, Ситх: %s' % (self.recruit, self.sith)

    class Meta:
        verbose_name = 'Рука тени'
        verbose_name_plural = 'Руки тени'

class Question(models.Model):
    title = models.CharField(max_length=1024, verbose_name='Вопрос')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    
class Test(models.Model):
    order_code = models.IntegerField(unique=True, verbose_name='Уникальный код ордена')
    question = models.ManyToManyField(Question, max_length=250, verbose_name='Вопрос/Вопросы')
    visible = models.BooleanField(default=True, verbose_name='Видимость')

    def __str__(self):
        return str(self.order_code)
    
    class Meta:
        verbose_name = 'Тестовое испытание'
        verbose_name_plural = 'Тестовые испытания'

class Variant(models.Model):
    question = models.ForeignKey(Question, on_delete=models.PROTECT, verbose_name='Вопрос')
    title = models.CharField(max_length=1024, verbose_name='Вариант ответа')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Вариант ответва'
        verbose_name_plural = 'Варианты ответа'

class Answer(models.Model):
    recruit = models.ForeignKey(Recruit, on_delete=models.PROTECT)
    test = models.ForeignKey(Test, on_delete=models.PROTECT)
    question = models.ForeignKey(Question, on_delete=models.PROTECT)
    variant = models.ForeignKey(Variant, null=True, on_delete=models.PROTECT)

    def __str__(self):
        return 'Рекрут: %s, Тест: %s Вопрос: %s, Ответ: %s' % (self.recruit, self.test, self.question, self.variant)

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'

class Result(models.Model):
    recruit = models.ForeignKey(Recruit, on_delete=models.PROTECT, verbose_name='Рекрут')
    test = models.ForeignKey(Test, on_delete=models.PROTECT, verbose_name='Тестовое испытания')
    mark_as_pass = models.BooleanField(default=False, verbose_name='Отметка о прохождение')

    def __str__(self):
        return '%s, %s' % (self.recruit, self.test)

    class Meta:
        verbose_name = 'Результат'
        verbose_name_plural = 'Результаты'