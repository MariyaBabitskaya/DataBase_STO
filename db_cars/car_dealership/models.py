from django.db import models

class People(models.Model):
    first_name = models.CharField(max_length=30, verbose_name='Имя')
    ser_name = models.CharField(max_length=30, verbose_name='Фамилия')
    patronymiс = models.CharField(max_length=30, verbose_name='Отчество')
    city = models.CharField(max_length=20, verbose_name='Город')

    def __str__(self):
        return f'{self.first_name} {self.ser_name} {self.patronymiс} -- {self.city}'

    class Meta:
        verbose_name = 'Список людей'
        verbose_name_plural = 'Список людей'

class CarsModels(models.Model):
    cars_model = models.CharField(max_length=30, verbose_name='Модель машины')

    def __str__(self):
        return self.cars_model

    class Meta:
        verbose_name = 'Модели машин'
        verbose_name_plural = 'Модели машин'

class Customers(models.Model):
    customer = models.ForeignKey(People, on_delete=models.CASCADE, verbose_name='Заказчик')
    car = models.ForeignKey(CarsModels, on_delete=models.CASCADE, verbose_name='Модель машины')
    data_order = models.DateField(verbose_name='Дата заказа')

    def __str__(self):
        return f'{self.id} - {self.customer} - {self.car} - {self.data_order}'

    class Meta:
        verbose_name = 'Заказчик и дата'
        verbose_name_plural = 'Заказчики и даты заказа'

class Works(models.Model):
    type_of_work = models.CharField(max_length=120, verbose_name='Вид услуги')
    price = models.IntegerField(help_text='цена в BYN', verbose_name='Цена')

    def __str__(self):
        return f'{self.type_of_work} -- {self.price} BYN'

    class Meta:
        verbose_name = 'Вид услуги в СТО'
        verbose_name_plural = 'Виды услуг в СТО'

class Orders(models.Model):
    works = models.ManyToManyField(Works, verbose_name='Виды работ')
    cust = models.ForeignKey(Customers, on_delete=models.CASCADE, verbose_name='Заказчик')

    def __str__(self):
        return f'{self.cust}'

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

