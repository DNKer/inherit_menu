from django.db import models


class Menu(models.Model):
    """
    Корневое меню.
    """
    title = models.CharField(
        max_length=255,
        unique=True,
        verbose_name='Имя меню',
    )
    url = models.CharField(
        max_length=255,
        verbose_name='URL меню',
        default=title,
    )

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'

    def __str__(self):
        return self.title


class Item(models.Model):
    """
    Дочернее меню (подменю).
    """
    title = models.CharField(
        max_length=255,
        verbose_name='Имя подменю',
    )
    url = models.CharField(
        max_length=255,
        verbose_name='URL подменю',
        default=title,
    )
    menu = models.ForeignKey(
        Menu, blank=True,
        related_name='items',
        on_delete=models.CASCADE,
        verbose_name='Название меню',
    )
    parent = models.ForeignKey(
        'self',
        blank=True,
        null=True,
        related_name='parents',
        on_delete=models.CASCADE,
        verbose_name='Родитель',
    )

    class Meta:
        verbose_name = 'Элемент меню'
        verbose_name_plural = 'Элементы меню'

    def __str__(self):
        return self.title
