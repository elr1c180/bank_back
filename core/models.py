from django.db import models

CATEGORY_CHOICES =( 
    ("1", "Marketing"), 
    ("2", "System"), 
    ("3", "Geography"), 

) 

class User(models.Model):
    chat_id = models.IntegerField()
    username = models.CharField(max_length=250, verbose_name='Username')
    first_name = models.CharField(max_length=250, verbose_name='Имя')
    last_name = models.CharField(max_length=250, verbose_name='Фамилия')
    is_referal = models.BooleanField(verbose_name='Реферал', null=True, blank=True)
    balance = models.IntegerField('Баланс', default=0)
    energy = models.IntegerField('Энергия', default=1000)
    tap_count = models.IntegerField('Очки/Нажатие', default=1)
    energy_level = models.ForeignKey("EnergyLevel", on_delete=models.CASCADE, verbose_name='Уровень энергии', null=True, blank=True)
    tap_level = models.ForeignKey("TapLevel", on_delete=models.CASCADE, verbose_name='Уровень нажатия', null=True, blank=True)
    total_per_hour= models.IntegerField('Заработок за секунду', default=0)
    referals = models.ManyToManyField('User', verbose_name='Рефералы пользователя', blank=True, null=True)
    task_list = models.ManyToManyField('Tasks', verbose_name='Список выполненных заданий', blank=True, null=True)
    level = models.ForeignKey('Level', on_delete=models.CASCADE, verbose_name='Уровень')


    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username

class EnergyLevel(models.Model):
    energy_level = models.IntegerField('Уровень энергии', default=1)
    price = models.IntegerField('Цена за повышение уровня', default = 1)

    class Meta:
        verbose_name = 'Уровень энергии'
        verbose_name_plural = 'Уровни энергии'
    
    def __str__(self):
        return str(self.energy_level)

class TapLevel(models.Model):
    tap_level = models.IntegerField('Уровень нажатия', default=1)
    price = models.IntegerField('Цена за повышение уровня', default = 1)

    class Meta:
        verbose_name = 'Уровень нажатия'
        verbose_name_plural = 'Уровни нажатия'
    
    def __str__(self):
        return str(self.tap_level)

class Level(models.Model):
    title = models.CharField(verbose_name='Название уровня', max_length=250)
    level = models.IntegerField(verbose_name='Уровень')
    min_balance = models.IntegerField(verbose_name='Минимальный баланс для получения уровня')
    max_balance = models.IntegerField(verbose_name='Максимальный баланс для уровня')

    class Meta:
        verbose_name = 'Уровень'
        verbose_name_plural = 'Уровни'

    def __str__(self):
        return self.title

class Tasks(models.Model):
    title = models.CharField(verbose_name='Название задания', max_length=250)
    url = models.CharField(verbose_name='Ссылка', max_length=1000)
    social_network = models.ForeignKey('Social_Network', on_delete=models.CASCADE, verbose_name='Соц. сеть')
    earn = models.IntegerField('Вознаграждение за задание', default=0)
    icon = models.ImageField(upload_to='', verbose_name='Изображение для задания', null=True, blank=True)

    left_gradient = models.CharField(verbose_name='Левый цвет', max_length=250)
    right_gradient = models.CharField(verbose_name='Правый цвет', max_length=250)

    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'

    def __str__(self):
        return self.title

class Social_Network(models.Model):
    title = models.CharField(verbose_name='Название социальной сети', max_length=250)

    class Meta:
        verbose_name = 'Соц. сеть'
        verbose_name_plural = 'Соц. сети'

    def __str__(self):
        return self.title

class Card(models.Model):
    title = models.CharField(verbose_name='Название карточки', max_length=250)
    img = models.ImageField(upload_to='', verbose_name='Изображение карточки')
    price = models.IntegerField(verbose_name='Прайс за карточку')
    earn_per_hour = models.IntegerField(verbose_name='Прибыль в час')

    first_gradient = models.CharField(verbose_name='Верхний градиент', max_length=250)
    second_gradient = models.CharField(verbose_name='Нижний градиент', max_length=250)

    category = models.CharField(verbose_name='Категория', choices=CATEGORY_CHOICES, max_length=250, null=True, blank=True)

    class Meta:
        verbose_name = 'Карточка'
        verbose_name_plural = 'Карточки'

    
    def __str__(self):
        return self.title