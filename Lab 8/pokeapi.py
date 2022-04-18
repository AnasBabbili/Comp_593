import requests

def get_poke_info(poke_name):
    """
    Gets all information about a specified pokemon

    :param name: Pokemon name
    :returns: Dictionary of pokemon info, if successful. None, if not
    """
    print("Getting Pokemon information...", end='')
    URL = 'https://pokeapi.co/api/v2/pokemon/'

    response = requests.get(URL + poke_name)

    if response.status_code == 200:
        print("Sucess")
        return response.json()
    else:
        print("Failed. Invalid Pokemon name entered. Try again")
        return