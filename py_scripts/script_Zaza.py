# getting probable gender assigned to characters that wikipedia already assigns gender for

import json
from urllib import request, parse
from collections import Counter

import json

with open('filtered_characters.json', encoding='utf-8') as filtered_json:
    filter_by_fic_character = json.load(filtered_json)

for character_dictionary in filter_by_fic_character:
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
            if he_him > 0 and she_her == 0:
                character_dictionary['probable gender'] = 'ontology/Male'
                print("Probably male")
            elif she_her > 0 and he_him == 0: 
                character_dictionary['probable gender'] = 'ontology/Female'
                print("Probably female")
            else:
                print("Can't figure out gender")
        else:
            print(data)
    # else:
        # print(f"{character_dictionary['title']} already has gender")

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
                character_dictionary['ontology/gender'] = character_dictionary["ontology/gender" ].split("/")[-1]
                character_dictionary['probable gender'] = character_dictionary["probable gender" ].split("/")[-1]

with open('probable_comparison.json','w',encoding='utf-8')as file:
    json.dump(filtered_dictionaryCHARAC_GEN,file, indent = 4)

# for character in filtered_dictionaryCHARAC_GEN:
#         filtered_dictionary_CHARAC_GEN_FOR_CSV_altered.append({
#             'fic_character': filtered_dictionaryCHARAC_GEN[character]['title'],
#             'gender' : filtered_dictionaryCHARAC_GEN[character]['ontology/gender'],
#             'probable gender': filtered_dictionaryCHARAC_GEN[character]['probable gender']
#         })
# import csv

# with open('dictionary_fictional_characters_gender_probable.csv', 'w', newline='') as file:
#     fieldnames = ['fic_character', 'gender', 'probable gender']
#     writer = csv.DictWriter(file, fieldnames=fieldnames)
#     writer.writeheader()
#     for item in filtered_dictionary_CHARAC_GEN_FOR_CSV_altered:
#         writer.writerow(item)
