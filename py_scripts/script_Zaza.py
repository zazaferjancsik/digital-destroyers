# getting probable gender assigned to characters that wikipedia already assigns gender for
# using API and urllib to import extractions

import json
from urllib import request, parse
from collections import Counter

import json

with open('filtered_characters.json', encoding='utf-8') as filtered_json:
    filter_by_fic_character = json.load(filtered_json)

for character_dictionary in filter_by_fic_character:
# if ontology/gender is present as key --> use that character to also assign probable gender based on pronouns
    if 'ontology/gender' in character_dictionary:
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
# if he or him more occuring than she her and she her is not present, assign probable gender Male
            if he_him > 0 and she_her == 0:
                character_dictionary['probable gender'] = 'ontology/Male'
                print("Probably male")
# if she or her more occuring than he him and he him is not present, assign probable gender Female
            elif she_her > 0 and he_him == 0: 
                character_dictionary['probable gender'] = 'ontology/Female'
                print("Probably female")
            else:
                print("Can't figure out gender")
        else:
            print(data)
    # else:
        # print(f"{character_dictionary['title']} already has gender")

# add new dictionary with added key 'probable gender' to it into json file --> TO BE USED IN 'script_comparison_probable.py'

with open('filtered_characters_altered.json','w',encoding='utf-8') as file:
    json.dump(filter_by_fic_character,file, indent = 4)



# #import and open to read json file (DBpeople filtered for fictional characters)

with open('filtered_characters_altered.json', encoding='utf-8') as filtered_probable_json:
    filter_by_fic_character = json.load(filtered_probable_json)

# create an empty dictionary to add all the filtered characters to by gender and probable gender
filtered_dictionaryCHARAC_GEN= {}
filtered_dictionary_CHARAC_GEN_FOR_CSV_altered = []

for character_dictionary in filter_by_fic_character:
        if "probable gender" in character_dictionary:
            if type(character_dictionary['ontology/gender']) == list:
                 pass
            else:
                filtered_dictionaryCHARAC_GEN[character_dictionary['title']] = character_dictionary
# ontology set as string with / and gender is last item in the string, so take the -1 item (last item)
                character_dictionary['ontology/gender'] = character_dictionary["ontology/gender" ].split("/")[-1]
                character_dictionary['probable gender'] = character_dictionary["probable gender" ].split("/")[-1]
# For ontology/gender specified by Wikipedia as something other than Female or Male, assign Female or Male
                if character_dictionary['ontology/gender'] == 'Girl':
                    character_dictionary['ontology/gender'] = 'Female'
                if character_dictionary['ontology/gender'] == 'Man':
                    character_dictionary['ontology/gender'] = 'Male'
                    
# edit json file and dump into the json file: ontology/gender and probable gender now only contain the word Male or Female
with open('probable_comparison.json','w',encoding='utf-8')as file:
    json.dump(filtered_dictionaryCHARAC_GEN,file, indent = 4)


# --> JSON FILE TO BE USED IN PYTHON SCRIPT: 'script_comparison_probable.py'

