import requests
from tkinter import *
from tkinter import ttk

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
        #print("Failed. Incorrect Pokemon name entered. Try again")
        root = Tk()
        root.geometry('300x100')
        error_frm = ttk.Frame(root)
        error_frm.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        error_msg = ttk.Label(error_frm, text = "Invalid Pokemon name enterd. Try again")
        error_msg.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
        return