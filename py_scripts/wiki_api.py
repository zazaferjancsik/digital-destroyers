# import json and urllib and collections as below to be able to use API and extract summaries
import json
from urllib import request, parse
from collections import Counter

# open the filtered_characters json file --> oldest version of filtered characters, has no probable gender or start years
with open('filtered_characters.json', encoding='utf-8') as filtered_json:
    filter_by_fic_character = json.load(filtered_json)

for character_dictionary in filter_by_fic_character:
# if Wikipedia already assigned a gender to the character, do not assign using pronouns but skip: try and except used so code/program does not crash
    if 'ontology/gender' not in character_dictionary:
# use API and extract summaries using url_title
        url_title = parse.quote_plus(character_dictionary['title'])
        try:
            with request.urlopen(f"https://en.wikipedia.org/api/rest_v1/page/summary/{url_title}") as webpage:
                data = json.load(webpage)
        except:
# if no summary found, print:
            print(f"Page for {character_dictionary['title']} not found")
            data = {}   

# if summary found (extract), print that it is found and set all capital letters to lowercase (no unique) count the pronouns. 
        if 'extract' in data:
# if extract found, print that that character's page has been found
            print(f"Got page for {character_dictionary['title']}")
# set word count and make all lower case so all not unique
            word_counts = Counter(data["extract"].lower().split())
            he_him = word_counts.get("he", 0) + word_counts.get("him", 0)
            she_her = word_counts.get("she", 0) + word_counts.get("her", 0)
# if he or him more occuring than she her and she her is not present, assign  ontology/gender Male
            if he_him > 0 and she_her == 0:
                character_dictionary['ontology/gender'] = 'ontology/Male'
                print("Probably male")
# if she or her more occuring than he him and he him is not present, assign ontology/gender Female
            elif she_her > 0 and he_him == 0: 
                character_dictionary['ontology/gender'] = 'ontology/Female'
                print("Probably female")
            else:
                print("Can't figure out gender")
        else:
            print(data)
    else:
# if wikipedia had already assigned gender, state so:
        print(f"{character_dictionary['title']} already has gender")

# add ontology/gender to json file
with open('filtered_characters_augmented.json','w',encoding='utf-8') as file:
    json.dump(filter_by_fic_character,file, indent = 4)

# JSON FILE TO BE USED IN SCRIPT 'script_Annalisa.py'