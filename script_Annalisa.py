# FIRST --> do current representation,
# LATER --> split up for bias etc, when it appeared
# current representation: fictional characters, gender, csv, R, visualisation

#import and open to read json file (DBpeople filtered for fictional characters)

import json

with open('filtered_characters_augmented.json', encoding='utf-8') as filtered_json:
    filter_by_fic_character = json.load(filtered_json)

# create an empty dictionary to add all the filtered characters to by gender
filtered_dictionaryCHARAC_GEN= {}
filtered_dictionary_CHARAC_GEN_FOR_CSV = []

for character_dictionary in filter_by_fic_character:
    for gender in character_dictionary:
# json file specifies per ontology/gender so filter for this in the filtered dictionary
        if "ontology/gender" in gender:
            if type(character_dictionary[gender]) == list and gender != 'ontology/gender_label':
                for character_number in [0, len(character_dictionary[gender])-1]:
                    name = character_dictionary['title'].split('_')
                    filtered_dictionaryCHARAC_GEN[name[character_number*2]] = character_dictionary.copy()
                    filtered_dictionaryCHARAC_GEN[name[character_number*2]][gender] = character_dictionary[gender][character_number]
                    filtered_dictionaryCHARAC_GEN[name[character_number*2]]['ontology/gender'] = filtered_dictionaryCHARAC_GEN[name[character_number*2]]["ontology/gender" ].split("/")
# only want last entry so reverse (Male/Female appears last in gender ontology)
                    filtered_dictionaryCHARAC_GEN[name[character_number*2]]["ontology/gender" ].reverse()
                    filtered_dictionaryCHARAC_GEN[name[character_number*2]]["ontology/gender" ] =   filtered_dictionaryCHARAC_GEN[name[character_number*2]]["ontology/gender" ][0]
                    filtered_dictionary_CHARAC_GEN_FOR_CSV.append({
                        'fic_character': filtered_dictionaryCHARAC_GEN[name[character_number*2]]['title'],
                        'gender' : filtered_dictionaryCHARAC_GEN[name[character_number*2]]['ontology/gender']
                #'start_year': filtered_dictionaryCHARAC_GEN[character]['start_year']
                        })
            elif type(character_dictionary[gender]) == list and gender == 'ontology/gender_label':
                pass
            else:
                filtered_dictionaryCHARAC_GEN[character_dictionary['title']] = character_dictionary
# only want Male/Female for gender specification so split by /
        # if type(filtered_dictionaryCHARAC_GEN[letter['title']]['ontology/gender']) == list:
        #     for i in 
                filtered_dictionaryCHARAC_GEN[character_dictionary['title']]['ontology/gender'] = filtered_dictionaryCHARAC_GEN[character_dictionary['title']]["ontology/gender" ].split("/")
# only want last entry so reverse (Male/Female appears last in gender ontology)
                filtered_dictionaryCHARAC_GEN[character_dictionary['title']]["ontology/gender" ].reverse()
                filtered_dictionaryCHARAC_GEN[character_dictionary['title']]["ontology/gender" ] =   filtered_dictionaryCHARAC_GEN[character_dictionary['title']]["ontology/gender" ][0]
                filtered_dictionary_CHARAC_GEN_FOR_CSV.append({
                    'fic_character': filtered_dictionaryCHARAC_GEN[character_dictionary['title']]['title'],
                    'gender' : filtered_dictionaryCHARAC_GEN[character_dictionary['title']]['ontology/gender']
                    #'start_year': filtered_dictionaryCHARAC_GEN[character]['start_year']
                    })

# filtered_dictionary_CHARAC_GEN_FOR_CSV['gender'] = filtered_dictionaryCHARAC_GEN[letter['ontology/gender']]
# only want last entry so reverse (Male/Female appears last in gender ontology)
       
# not all characters have a start year for the series/movie --> use external dataset to obtain information
# external dataset from Imdb for startyear of item (tsv file)
# count = 0
# with open('title.basics.tsv') as file:         
#     for line in file:
#         for character in filtered_dictionaryCHARAC_GEN:
# # if the name is the same for line in the imdb dataset to the name of item in DBpeople file, add the start year for the item to the dictionary made for the fictional characters
#             if 'ontology/firstAppearance' in filtered_dictionaryCHARAC_GEN[character]:
#                 if line.split('\t')[2] == filtered_dictionaryCHARAC_GEN[character]['ontology/firstAppearance']:
#                     if line.split('\t')[5] != '\\N':
#                         filtered_dictionaryCHARAC_GEN[character]['start_year'] = int(line.split('\t')[5])
#                         filtered_dictionary_CHARAC_GEN_FOR_CSV.append({
#                                 'fic_character': filtered_dictionaryCHARAC_GEN[character]['title'],
#                                 'gender' : filtered_dictionaryCHARAC_GEN[character]['ontology/gender'],
#                                 'start_year': filtered_dictionaryCHARAC_GEN[character]['start_year']
#                             })
#                         print("Done for "+str(filtered_dictionaryCHARAC_GEN[character]['title'])+ " line: "+ str(count))
#         count += 1
import csv

with open('dictionary_fictional_characters_gender.csv', 'w', newline='') as file:
    fieldnames = ['fic_character', 'gender']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    for item in filtered_dictionary_CHARAC_GEN_FOR_CSV:
        writer.writerow(item)
