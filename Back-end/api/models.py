from django.db import models
from django.contrib.auth.models import AbstractUser


class Club(models.Model):
    name = models.CharField(max_length=100)
    points = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name} ({self.points} points)"

class Match(models.Model):
    home_club = models.ForeignKey(Club, related_name='home_matches', on_delete=models.CASCADE)
    away_club = models.ForeignKey(Club, related_name='away_matches', on_delete=models.CASCADE)
    match_date = models.DateTimeField()
    state1=models.IntegerField(default=0)
    state2=models.IntegerField(default=0)
    state3=models.IntegerField(default=0)

    def __str__(self):
        return f"{self.home_club.name} vs {self.away_club.name} on {self.match_date} with states {self.state1}, {self.state2}, {self.state3}"


class MyUser(AbstractUser):
    balance=models.IntegerField()
    name=models.CharField(max_length=255)
    email=models.CharField(max_length=255,unique=True)
    password=models.CharField(max_length=255)
    username =None

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]
    def __str__(self):
        return f"{self.email} - Balance: {self.balance}"
    
class Bet(models.Model):
    match = models.ForeignKey(Match, related_name='bets', on_delete=models.CASCADE)
    state_chosen=models.IntegerField(default=0)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    user = models.ForeignKey(MyUser, related_name='bets', on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.user.username} bets {self.amount} on {self.match} with chosen state {self.state_chosen}"
