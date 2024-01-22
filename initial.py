import json

dictionary = {
    'A_people':{},
    'B_people':{},
    'C_people':{},
    'D_people':{},
    'E_people':{},
    'F_people':{},
    'G_people':{},
    'H_people':{},
    'I_people':{},
    'J_people':{},
    'K_people':{},
    'L_people':{},
    'M_people':{},
    'N_people':{},
    'O_people':{},
    'P_people':{},
    'Q_people':{},
    'R_people':{},
    'S_people':{},
    'T_people':{},
    'U_people':{},
    'V_people':{},
    'W_people':{},
    'X_people':{},
    'Y_people':{},
    'Z_people':{},
}
characters = ['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M','N', 'P', 'Q', 'R', 'S','T', 'U', 'O', 'V', 'W', 'X', 'Y', 'Z']
#for character in characters:
    #with open(f'People/{character}_people.json',encoding='utf-8')as file:
        #contents = file.read()
with open('People/Z_people.json',encoding='utf-8')as file:
    contents = json.load(file)
character = []
for content in contents:
        if "http://www.w3.org/1999/02/22-rdf-syntax-ns#type_label" in content:
              for list in content["http://www.w3.org/1999/02/22-rdf-syntax-ns#type_label"]:
                    if 'fictional character'in list:
                        character.append(content)
print(character)
            
