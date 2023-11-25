from django.shortcuts import render,redirect,get_object_or_404
from .models import BoardGame
from .models import BoardGame, GameLoan,BoardGamer
from .forms import BoardGameForm, EditBoardGameForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    """The home page for game."""
    return render(request, 'gamers/index.html')
def games(request):
    """Show all games."""
    games = BoardGame.objects.order_by('created_at').all()
    borrowed_games = GameLoan.objects.filter(gamer=request.user.boardgamer, returned=False)
    context = {'games': games, 'borrowed_games': borrowed_games}
    return render(request, 'gamers/games.html', context)

@login_required
def add_game(request):
    if request.method == 'POST':
        form = BoardGameForm(request.POST)
        if form.is_valid():
            game = form.save()
            return redirect('gamers:games')
    else:
        form = BoardGameForm()
    return render(request, 'gamers/add_game.html',{'form': form})
@login_required
def edit_game(request, game_id):
  
    game = BoardGame.objects.get(id=game_id)
    if request.method == 'POST':
        form = EditBoardGameForm(request.POST,instance=game )
        if form.is_valid():
            form.save()
            return redirect('gamers:games')

    else:
        form = EditBoardGameForm(instance=game)

    return render(request, 'gamers/edit_game.html', {'form': form, "game":game})
@login_required
def delete_game(request, game_id):
    game = BoardGame.objects.get(id=game_id)
    
    if request.method == 'POST':
        game.delete()
        return redirect('gamers:games')
    
    return render(request, 'gamers/delete_game.html', {'game': game})
@login_required
def borrow_game(request, game_id):
   
    game = get_object_or_404(BoardGame, pk=game_id)
    gamer, created = BoardGamer.objects.get_or_create(user=request.user)
    if GameLoan.objects.filter(gamer=gamer, game=game, returned=False).exists():
        message = 'You have already borrowed this game.'
    elif GameLoan.objects.filter(gamer=gamer, returned=False).count() >= 3:
        message = 'You can\'t borrow more than 3 games.'
    else:
        # User can borrow the game
        loan = GameLoan.objects.create(gamer=gamer, game=game)
        return redirect('gamers:games')

    # If there's a message or any issue, render the games page with the message
    games = BoardGame.objects.all()
    borrowed_games = GameLoan.objects.filter(gamer=gamer, returned=False)
    return render(request, 'gamers/games.html', {'games': games, 'message': message, 'borrowed_games': borrowed_games})
@login_required
def return_game(request, loan_id):
    loan = get_object_or_404(GameLoan, pk=loan_id)
    if loan.gamer.user != request.user:
        return redirect('gamers:games')
    loan.returned = True
    loan.save()
    return redirect('gamers:games')
   