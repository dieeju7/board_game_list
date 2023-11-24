from django.contrib import admin

from .models import BoardGame, BoardGamer, GameLoan

admin.site.register(BoardGame)
admin.site.register(BoardGamer)
admin.site.register(GameLoan)
