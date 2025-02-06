from django.db import models

class Person(models.Model):
    name=models.CharField(max_length=20)
    money=models.IntegerField()
    bet=models.IntegerField()
    bet_to=models.CharField(max_length=20)
    double_btn=models.BooleanField(default=True)

class Odds(models.Model):
    match_num=models.IntegerField()
    money_opt1=models.IntegerField(default=1)
    money_opt2=models.IntegerField(default=1)
    money_opt3=models.IntegerField(default=1)
    money_opt4=models.IntegerField(default=1)
    odds_opt1=models.FloatField(default=0)
    odds_opt2=models.FloatField(default=0)
    odds_opt3=models.FloatField(default=0)
    odds_opt4=models.FloatField(default=0)
    total_money=models.IntegerField(default=0)
