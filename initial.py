import json
characters = ['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M','N', 'P', 'Q', 'R', 'S','T', 'U', 'O', 'V', 'W', 'X', 'Y', 'Z']
#for character in characters:
    #with open(f'People/{character}_people.json',encoding='utf-8')as file:
        #contents = file.read()
character = []
for alphabet in characters:
    with open(f'People/{alphabet}_people.json',encoding='utf-8')as file:
        contents = json.load(file)
    for content in contents:
            if "http://www.w3.org/1999/02/22-rdf-syntax-ns#type_label" in content:
                for list in content["http://www.w3.org/1999/02/22-rdf-syntax-ns#type_label"]:
                        if 'fictional character'in list:
                            character.append(content)
with open('filtered_characters.json','w',encoding='utf-8')as file:
    json.dump(character,file)
