import requests

class CardService:
  base_url = 'https://api.scryfall.com/cards'

  def search_cards(name):
    url = 'https://api.scryfall.com/cards/named?'
    params = {'fuzzy': name}
    response = requests.get(url, params=params)

    if response.status_code == 200:
      return [response.json()]
    else:
      return []
    
    # potentially create an autocomplete route service to a list of potential options