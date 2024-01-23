import json

with open('filtered_characters.json', encoding='utf-8') as filtered_json:
    filter_by_fic_character = json.load(filtered_json)

# create an empty dictionary to add all the filtered characters to by gender
filtered_dictionaryCHARAC_MYTH= {}
filtered_dictionary_CHARAC_MYTH_FOR_CSV = []

for character_dictionary in filter_by_fic_character:
    for mytho in character_dictionary:
# json file specifies per ontology/gender so filter for this in the filtered dictionary
        if "ontology/mythology" in mytho:
            if type(character_dictionary[mytho]) == list and mytho != 'ontology/mythology_label':
                for character_number in [0, len(character_dictionary[mytho])-1]:
                    name = character_dictionary['title'].split('_')
                    filtered_dictionaryCHARAC_MYTH[name[character_number*2]] = character_dictionary.copy()
                    filtered_dictionaryCHARAC_MYTH[name[character_number*2]][mytho] = character_dictionary[mytho][character_number]
                    filtered_dictionaryCHARAC_MYTH[name[character_number*2]]['ontology/mythology'] = filtered_dictionaryCHARAC_MYTH[name[character_number*2]]["ontology/mythology" ].split("/")
# only want last entry so reverse (Male/Female appears last in gender ontology)
                    filtered_dictionaryCHARAC_MYTH[name[character_number*2]]["ontology/mythology" ].reverse()
                    filtered_dictionaryCHARAC_MYTH[name[character_number*2]]["ontology/mythology" ] =   filtered_dictionaryCHARAC_MYTH[name[character_number*2]]["ontology/mythology" ][0]
                    filtered_dictionary_CHARAC_MYTH_FOR_CSV.append({
                            'fic_character': name[character_number*2],
                            'mythology' : filtered_dictionaryCHARAC_MYTH[name[character_number*2]]["ontology/mythology" ]
                        })
            elif type(character_dictionary[mytho]) == list and mytho == 'ontology/mythology_label':
                pass
            else:
                filtered_dictionaryCHARAC_MYTH[character_dictionary['title']] = character_dictionary
# only want Male/Female for gender specification so split by /
        # if type(filtered_dictionaryCHARAC_GEN[letter['title']]['ontology/gender']) == list:
        #     for i in 
                filtered_dictionaryCHARAC_MYTH[character_dictionary['title']]['ontology/mythology'] = filtered_dictionaryCHARAC_MYTH[character_dictionary['title']]["ontology/mythology" ].split("/")
# only want last entry so reverse (Male/Female appears last in gender ontology)
                filtered_dictionaryCHARAC_MYTH[character_dictionary['title']]["ontology/mythology" ].reverse()
                filtered_dictionaryCHARAC_MYTH[character_dictionary['title']]["ontology/mythology" ] =   filtered_dictionaryCHARAC_MYTH[character_dictionary['title']]["ontology/mythology" ][0]
                filtered_dictionary_CHARAC_MYTH_FOR_CSV.append({
                        'fic_character': character_dictionary['title'],
                        'mythology' : character_dictionary['ontology/mythology']
                    })
import csv

with open('dictionary_fictional_characters_mythology.csv', 'w', newline='') as file:
    fieldnames = ['fic_character', 'mythology']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    for item in filtered_dictionary_CHARAC_MYTH_FOR_CSV:
        writer.writerow(item)