import json
from urllib import request, parse
from collections import Counter

import json

with open('filtered_characters.json', encoding='utf-8') as filtered_json:
    filter_by_fic_character = json.load(filtered_json)

for character_dictionary in filter_by_fic_character:
    if 'ontology/gender' not in character_dictionary:
        url_title = parse.quote_plus(character_dictionary['title'])
        try:
            with request.urlopen(f"https://en.wikipedia.org/api/rest_v1/page/summary/{url_title}") as webpage:
                data = json.load(webpage)
        except:
            print(f"Page for {character_dictionary['title']} not found")
            data = {}   

        if 'extract' in data:
            print(f"Got page for {character_dictionary['title']}")
            word_counts = Counter(data["extract"].lower().split())
            he_him = word_counts.get("he", 0) + word_counts.get("him", 0)
            she_her = word_counts.get("she", 0) + word_counts.get("her", 0)
            if he_him > 0 and she_her == 0:
                character_dictionary['ontology/gender'] = 'ontology/Male'
                print("Probably male")
            elif she_her > 0 and he_him == 0: 
                character_dictionary['ontology/gender'] = 'ontology/Female'
                print("Probably female")
            else:
                print("Can't figure out gender")
        else:
            print(data)
    else:
        print(f"{character_dictionary['title']} already has gender")

with open('filtered_characters_augmented.json','w',encoding='utf-8') as file:
    json.dump(filter_by_fic_character,file, indent = 4)