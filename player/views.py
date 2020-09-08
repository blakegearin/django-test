from django.shortcuts import render

from gameplay.models import Game


def home(request):
    current_user_games = Game.objects.games_for_user(request.user)
    current_user_active_games = current_user_games.active()

    return render(
        request,
        "player/home.html",
        {
            'username': request.user.username,
            'games': current_user_active_games
        }
    )
