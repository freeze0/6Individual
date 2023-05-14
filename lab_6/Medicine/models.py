from django.db import models


class Human(models.Model):
    class Meta:
        verbose_name = "Пациент"
        verbose_name_plural = "Пациенты"

    id_human = models.AutoField(verbose_name='ID Человека', primary_key=True, unique=True)
    name = models.CharField(verbose_name='Имя', max_length=255)
    surname = models.CharField(verbose_name='Фамилия', max_length=255)
    reason = models.CharField(verbose_name='Причина:', max_length=255)

    def __str__(self):
        return f"{self.name} {self.surname}"


class Doctor(models.Model):
    class Meta:
        verbose_name = "Доктор"
        verbose_name_plural = "Докторы"

    id_doctor = models.AutoField(verbose_name='ID Доктора', primary_key=True, unique=True)
    name = models.CharField(verbose_name='Имя', max_length=255)
    surname = models.CharField(verbose_name='Фамилия', max_length=255)
    specialty = models.CharField(verbose_name='Специальность:', max_length=255)

    def __str__(self):
        return f"{self.name} {self.surname}"

class Appointment(models.Model):
    class Meta:
        verbose_name = "Запись"
        verbose_name_plural = "Записи"

    id_app = models.AutoField(verbose_name='ID Записи', primary_key=True, unique=True)
    id_human = models.ForeignKey(Human, verbose_name='ID Человека', on_delete=models.SET(-1))
    id_doctor = models.ForeignKey(Doctor, verbose_name='ID Доктора', on_delete=models.SET(-1))
    app_time = models.DateField(verbose_name='Дата записи', max_length=255)

    def get_absolute_url(self):
        return f'/{self.id_app}/change'

    def __str__(self):
        return f" На приёме {self.id_human} у {self.id_doctor} {self.app_time}"