from django.db import models


class Yonalish(models.Model):
    nom = models.CharField(max_length=255)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.nom

    class Meta:
        verbose_name = 'Yonalish'
        verbose_name_plural = 'Yonalishlar'

class Fan(models.Model):
    nom = models.CharField(max_length=255)
    asosiy = models.BooleanField(default=False)
    yonalish = models.ForeignKey(Yonalish, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom

    class Meta:
        verbose_name = 'Fan'
        verbose_name_plural = 'Fanlar'

class Teacher(models.Model):
    name = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=255, choices=(('erkak','erkak'),('ayol','ayol')))
    daraja = models.CharField(max_length=255, choices=(('Bakalavr','Bakalavr'),('Magistr','Magistr')))
    fan = models.ForeignKey(Fan, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Teacher'
        verbose_name_plural = "Oqituvchilar"

