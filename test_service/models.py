from django.db import models

class Test(models.Model):
    """Тестовое испытание"""
    title = models.CharField(max_length=255, verbose_name='Наименование теста')
    order_code = models.CharField(max_length=255, unique=True, verbose_name='Уникальный код ордена')
    questions = models.ManyToManyField(to='Question', verbose_name='Вопросы')
    is_visible = models.BooleanField(default=True, verbose_name='Отображение')

    class Meta:
        verbose_name = 'Тестовое испытание'
        verbose_name_plural = 'Тестовые испытания'

    def __str__(self):
        return self.title

class Question(models.Model):
    """Вопросы"""
    title = models.CharField(max_length=2048, verbose_name='Вопрос')
    variants = models.ManyToManyField(to='Variant', verbose_name='Варианты ответов')

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'
    
    def __str__(self):
        return self.title

class Variant(models.Model):
    """Варианты ответов на вопросы"""
    title = models.CharField(max_length=1024, verbose_name='Вариант ответа')

    class Meta:
        verbose_name = 'Вариант ответа'
        verbose_name_plural = 'Варианты ответа'

    def __str__(self):
        return self.title

class Answer(models.Model):
    """Ответы на тест"""
    recruit = models.ForeignKey(to='recruiting_service.Recruit', verbose_name='Рекрут', on_delete=models.PROTECT)
    test = models.ForeignKey(to='Test', verbose_name='Тест', on_delete=models.PROTECT)
    question = models.ForeignKey(to='Question', verbose_name='Вопрос', on_delete=models.PROTECT)
    variant = models.ForeignKey(to='Variant', verbose_name='Вариант', on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Ответ на тест'
        verbose_name_plural = 'Ответы на тест'

    def __str__(self):
        return 'Рекрут: {recruit}, Тест: {test}, Вопрос: {question}, Ответ: {variant}'.format(recruit=self.recruit, test=self.test, question=self.question, variant=self.variant)

class Result(models.Model):
    """Результаты выполнения теста"""
    recruit = models.ForeignKey(to='recruiting_service.Recruit', verbose_name='Рекрут', on_delete=models.PROTECT)
    test = models.ForeignKey(to='Test', verbose_name='Тест', on_delete=models.PROTECT)
    mark_as_pass = models.BooleanField(default=False, verbose_name='Отметка о прохождение')
    datetime_of_completion = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время выполнения')

    class Meta:
        verbose_name = 'Результат'
        verbose_name_plural = 'Результаты'

    def __str__(self):
        return 'Рекрут: {recruit}, Тест: {test}, Дата и время выполнения: {datetime}'.format(recruit=self.recruit, test=self.test, datetime=self.datetime_of_completion)
