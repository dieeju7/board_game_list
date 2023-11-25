from django.urls import path

from . import views 

app_name ='gamers'
urlpatterns = [
    path('',views.index,name='index'),
    path('games/', views.games, name='games'),
    path('add_game/', views.add_game, name='add_game'),
    path('borrow_game/<int:game_id>/', views.borrow_game, name='borrow_game'),
    path('return_game/<int:game_id>/', views.return_game, name='return_game'),
    path('delete_game/<int:game_id>/', views.delete_game, name='delete_game'),
    path('edit_game/<int:game_id>/', views.edit_game, name='edit_game'),
]