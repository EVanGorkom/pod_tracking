"""
URL configuration for market_nextdoor_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from django.conf import settings
from .views import user_views, deck_views, card_views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    # user
    path('users', user_views.user_list),
    path('users/<int:user_id>', user_views.user_details),
    # user deck
    path('users/<int:user_id>/decks', deck_views.deck_list),
    path('users/<int:user_id>/decks/<int:deck_id>', deck_views.deck_details),
    # deck leaders (card)
    path('users/<int:user_id>/decks/<int:deck_id>/create_card', card_views.create_mtg_card),
    path('users/<int:user_id>/decks/<int:deck_id>/cmdr_details/<int:card_id>', card_views.mtg_card_details)
]

