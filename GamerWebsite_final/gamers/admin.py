from django.contrib import admin

from .models import BoardGame, BoardGamer, GameLoan

admin.site.register(BoardGame)
admin.site.register(BoardGamer)
class GameLoanAdmin(admin.ModelAdmin):
    list_display = ('gamer', 'game', 'loan_date', 'returned')
admin.site.register( GameLoan,GameLoanAdmin)