# FIRST --> do current representation,
# LATER --> split up for bias etc, when it appeared
# current representation: fictional characters, gender, csv, R, visualisations


#import and open to read json file (DBpeople filtered for fictional characters)

import json

with open('filtered_characters.json', encoding='utf-8') as filtered_json:
    filter_by_fic_character = json.load(filtered_json)

# create an empty dictionary to add all the filtered characters to by gender
filtered_dictionaryCHARAC_GEN= {}

for letter in filter_by_fic_character:
    for character in letter:
# json file specifies per ontology/gender so filter for this in the filtered dictionary
        if "ontology/gender" in character:
            if type(letter[character]) == list and character != 'ontology/gender_label':
                # letter['ontology/gender'] = letter['ontology/gender'].split("/")
                # letter['ontology/gender'] = letter['ontology/gender'].reverse
                # print(letter['ontology/gender'])
                for gender in [0, len(letter[character])-1]:
                    name = letter['title'].split('_')
                    filtered_dictionaryCHARAC_GEN[name[gender*2]] = letter.copy()
                    filtered_dictionaryCHARAC_GEN[name[gender*2]][character] = letter[character][gender]
                    filtered_dictionaryCHARAC_GEN[name[gender*2]]['ontology/gender'] = filtered_dictionaryCHARAC_GEN[name[gender*2]]["ontology/gender" ].split("/")
# only want last entry so reverse (Male/Female appears last in gender ontology)
                    filtered_dictionaryCHARAC_GEN[name[gender*2]]["ontology/gender" ].reverse()
                    filtered_dictionaryCHARAC_GEN[name[gender*2]]["ontology/gender" ] =   filtered_dictionaryCHARAC_GEN[name[gender*2]]["ontology/gender" ][0]
            elif type(letter[character]) == list and character == 'ontology/gender_label':
                pass
            else:
                filtered_dictionaryCHARAC_GEN[letter['title']] = letter
# only want Male/Female for gender specification so split by /
        # if type(filtered_dictionaryCHARAC_GEN[letter['title']]['ontology/gender']) == list:
        #     for i in 
                filtered_dictionaryCHARAC_GEN[letter['title']]['ontology/gender'] = filtered_dictionaryCHARAC_GEN[letter['title']]["ontology/gender" ].split("/")
# only want last entry so reverse (Male/Female appears last in gender ontology)
                filtered_dictionaryCHARAC_GEN[letter['title']]["ontology/gender" ].reverse()
                filtered_dictionaryCHARAC_GEN[letter['title']]["ontology/gender" ] =   filtered_dictionaryCHARAC_GEN[letter['title']]["ontology/gender" ][0]
                print(filtered_dictionaryCHARAC_GEN)

# for character in filtered_dictionaryCHARAC_GEN:
#     print(filtered_dictionaryCHARAC_GEN[character]["ontology/gender"])
# # not all characters have a start year for the series/movie --> use external dataset to obtain information
# # external dataset from Imdb for startyear of item (tsv file)
# with open('title.basics.tsv') as file:         
#     for character in filtered_dictionaryCHARAC_GEN:
#         for line in file:
# # if the name is the same for line in the imdb dataset to the name of item in DBpeople file, add the start year for the item to the dictionary made for the fictional characters
#             if line.split('\t')[2] == filtered_dictionaryCHARAC_GEN[character]['ontology/firstAppearance']:
#                 filtered_dictionaryCHARAC_GEN[character]['start_year'] = line[5]

