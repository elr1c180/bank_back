from django.db import models

class User(models.Model):
    chat_id = models.IntegerField()
    username = models.CharField(max_length=250, verbose_name='Username')
    first_name = models.CharField(max_length=250, verbose_name='Имя')
    last_name = models.CharField(max_length=250, verbose_name='Фамилия')
    balance = models.IntegerField('Баланс', default=0)
    energy = models.IntegerField('Энергия', default=1000)
    tap_count = models.IntegerField('Очки/Нажатие', default=1)
    task_list = models.ManyToManyField('Tasks', verbose_name='Список выполненных заданий')
    level = models.ForeignKey('Level', on_delete=models.CASCADE, verbose_name='Уровень')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username

class Level(models.Model):
    title = models.CharField(verbose_name='Название уровня', max_length=250)
    level = models.IntegerField(verbose_name='Уровень')
    min_balance = models.IntegerField(verbose_name='Минимальный баланс для получения уровня')

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

