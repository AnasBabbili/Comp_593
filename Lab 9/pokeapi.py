import requests

def get_pokemon_info(name):

    """
    Gets a ditionary of information from the PokeAPI or a specified pokemon.

    :param name: Pokemon's name 
    """
    print('Getting Pokemon information...', end='')

    if name is None:
        print('error: Missing name parameter')
        return

    name = name.strip().lower()
    if name == '':
        print('error: Empty name parameter')
        return

    URL = 'https://pokeapi.co/api/v2/pokemon/' + str(name)

    response = requests.get(URL)

    if response.status_code == 200:
        print('success')
        return response.json()
    else:
        print('failed')
        return

def get_pokemon_image_url(name):

    poke_dict = get_pokemon_info(name)
    if poke_dict:
        return poke_dict['sprites']['other']['official-artwork']['front_default']

def get_pokemon_list(limit=100, offset=0):

    url = 'https://pokeapi.co/api/v2/pokemon'
    
    params = {
        'limit': limit,
        'offset': offset
    }

    rsp_msg = requests.get(url, params=params)

    if rsp_msg.status_code == 200:
        
        dict = rsp_msg.json()

        return [p['name'] for p in dict['results']]
    else:
        print('Failed to get Pokemon list.')
        print('Response code:', rsp_msg.status_code)
        print(rsp_msg.text)

