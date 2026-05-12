from django.db import models

class PodsumowanieGraczy(models.Model):
    gracz = models.TextField(primary_key=True)
    ilosc = models.IntegerField()

    class Meta:
        managed = False  # bo to widok w bazie danych
        db_table = 'podsumowanie_graczy'

class Scoring(models.Model):
    id = models.IntegerField(primary_key=True)
    klan_id = models.IntegerField()
    chests = models.CharField(max_length=200)
    points = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'scoring'