from tkinter import *
from tkinter import ttk
from pokeapi import get_poke_info

def main():
    #create the window
    root = Tk()
    root.title("Pokemon Info Viewer")
    #root.iconbitmap("Poke-Ball.ico")

    #create the window frames
    usr_input_frm = ttk.Frame(root)
    usr_input_frm.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

    info_frm = ttk.LabelFrame(root, text='info')
    info_frm.grid(row=1, column=0, padx=10, pady=10, sticky=N)

    stats_frm = ttk.LabelFrame(root, text='stats')
    stats_frm.grid(row=1, column=1, padx=10, pady=10, sticky=N)

    #populate the widgets in the user input frame
    lbl_name = ttk.Label(usr_input_frm, text='Pokemon Name:')
    lbl_name.grid(row=0, column=0, padx=10, pady=10)

    ent_name = ttk.Entry(usr_input_frm)
    ent_name.grid(row=0, column=1, padx=(0,10), pady=10)

    #create button event
    def btn_get_info_click():
        #get the pokemon info from PokeApi
        pokemon_name = ent_name.get().lower()
        poke_dict = get_poke_info(pokemon_name)

        #populate displayed Pokemon values
        if poke_dict:
            lbl_height_val['text'] = str(poke_dict['height']) + ' dm'
            lbl_weight_val['text']= str(poke_dict['weight']) + ' hg'
            types_list = [t['type']['name'] for t in poke_dict['types']]
            lbl_type_val['text'] = ', '.join(types_list)
            prg_hp['value'] = poke_dict['stats'][0]['base_stat']
            prg_attack['value'] = poke_dict['stats'][1]['base_stat']
            prg_defense['value'] = poke_dict['stats'][2]['base_stat']
            prg_special_attack['value'] = poke_dict['stats'][3]['base_stat']
            prg_special_defense['value'] = poke_dict['stats'][4]['base_stat']
            prg_speed['value'] = poke_dict['stats'][5]['base_stat']


    btn_get_info = ttk.Button(usr_input_frm, text='Get Info', command=btn_get_info_click)
    btn_get_info.grid(row=0, column=2, padx=(0,10), pady=10)

    #populate the widgest in the info frame
    lbl_height = ttk.Label(info_frm, text='Height:')
    lbl_height.grid(row=0, column=0, pady=(5,0), stick=E)
    lbl_height_val = ttk.Label(info_frm)
    lbl_height_val.grid(row=0, column=1, pady=(5,0), sticky=W)

    lbl_weight = ttk.Label(info_frm, text='Weight:')
    lbl_weight.grid(row=2, column=0, pady=10, stick=E)
    lbl_weight_val = ttk.Label(info_frm)
    lbl_weight_val.grid(row=2, column=1, pady=10 ,sticky=W)

    lbl_type = ttk.Label(info_frm, text='Type:')
    lbl_type.grid(row=3, column=0, pady=(0,5), sticky=E)
    lbl_type_val = ttk.Label(info_frm, width=15)
    lbl_type_val.grid(row=3, column=1,  pady=(0,5), sticky=W)

    #populate the widgets in the stats frame
    lbl_hp = ttk.Label(stats_frm, text='HP:')
    lbl_hp.grid(row=0, column=0,  pady=(10,0), sticky=E)
    prg_hp = ttk.Progressbar(stats_frm, length=200, maximum=255)
    prg_hp.grid(row=0, column=1, pady=(10,0), sticky=W)

    lbl_attack = ttk.Label(stats_frm, text='Attack:')
    lbl_attack.grid(row=1, column=0, pady=10, sticky=E)
    prg_attack = ttk.Progressbar(stats_frm, length=200, maximum=255)
    prg_attack.grid(row=1, column=1,  pady=10, sticky=W)

    lbl_defense = ttk.Label(stats_frm, text='Defense:')
    lbl_defense.grid(row=2, column=0, sticky=E)
    prg_defense = ttk.Progressbar(stats_frm, length=200, maximum=255)
    prg_defense.grid(row=2, column=1, sticky=W)

    lbl_special_attack = ttk.Label(stats_frm, text='Special Attack:')
    lbl_special_attack.grid(row=3, column=0,  pady=10, sticky=E)
    prg_special_attack = ttk.Progressbar(stats_frm, length=200, maximum=255)
    prg_special_attack.grid(row=3, column=1,  pady=10, sticky=W)

    lbl_special_defense = ttk.Label(stats_frm, text='Special Defense:')
    lbl_special_defense.grid(row=4, column=0, sticky=E)
    prg_special_defense = ttk.Progressbar(stats_frm, length=200, maximum=255)
    prg_special_defense.grid(row=4, column=1, sticky=W)

    lbl_speed = ttk.Label(stats_frm, text='Speed:')
    lbl_speed.grid(row=5, column=0,  pady=10, sticky=E)
    prg_speed = ttk.Progressbar(stats_frm, length=200, maximum=255)
    prg_speed.grid(row=5, column=1,  pady=10, sticky=W)
    
    root.mainloop()

main()