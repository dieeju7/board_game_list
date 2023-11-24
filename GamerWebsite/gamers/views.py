from django.shortcuts import render,redirect
from .models import BoardGame
from .models import BoardGame, GameLoan,BoardGamer
from .forms import BoardGameForm, EditBoardGameForm
from django.contrib import messages
# Create your views here.
def index(request):
    """The home page for game."""
    return render(request, 'gamers/index.html')
def games(request):
    """Show all games."""
    games = BoardGame.objects.order_by('created_at')
    context = {'games': games}
    return render(request, 'gamers/games.html', context)

def add_game(request):
    if request.method == 'POST':
        form = BoardGameForm(request.POST)
        if form.is_valid():
            game = form.save()
            return redirect('gamers:games')
    else:
        form = BoardGameForm()
    return render(request, 'gamers/add_game.html',{'form': form})
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

def delete_game(request, game_id):
    game = BoardGame.objects.get(id=game_id)
    
    if request.method == 'POST':
        game.delete()
        return redirect('gamers:games')
    
    return render(request, 'gamers/delete_game.html', {'game': game})
    
def borrow_game(request, game_id):
    game = BoardGame.objects.get(id=game_id)

    borrowed_games = request.session.get('borrowed_games', [])

    if len(borrowed_games) <= 3 and game_id not in borrowed_games:
        borrowed_games.append(game_id)
        request.session['borrowed_games'] = borrowed_games
        return redirect('gamers:games')
    elif len(borrowed_games) > 3:
        message = 'You can only borrow up to 3 games at a time.'
    else:
        message = 'You have already borrowed this game.'

    messages.error(request, message)
    games = BoardGame.objects.all()

    return render(request, 'gamers/games.html', {'games': games})
def return_game(request, game_id):

    # loan =GameLoan.objects.get(id=loan_id)
    # loan.returned = True
    # loan.save()
    # return redirect('gamers:games')
    borrowed_games = request.session.get('borrowed_games', [])

    # Simulate returning logic
    if game_id in borrowed_games:
        borrowed_games.remove(game_id)
        request.session['borrowed_games'] = borrowed_games
        return redirect('gamers:games')
    else:
        games = BoardGame.objects.all()
        message = 'Game not found in your borrowed list.'
        return render(request, 'gamers/games.html', {'games': games, 'message': message})