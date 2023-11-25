from django.db import models
from django.contrib.auth.models import User

class BoardGame(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title

class BoardGamer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    borrowed_games = models.ManyToManyField(BoardGame, through='GameLoan')

    def __str__(self):
        return self.user.username

class GameLoan(models.Model):
    gamer = models.ForeignKey(BoardGamer, on_delete=models.CASCADE)
    game = models.ForeignKey(BoardGame, on_delete=models.CASCADE)
    loan_date = models.DateTimeField(auto_now_add=True)
    returned = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.gamer.user.username} borrowed {self.game.title}"
