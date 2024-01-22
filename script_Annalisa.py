# import and open to read json file (DBpeople filtered for fictional characters)

import json

with open() as filtered_json:
    filter_by_fic_character = filtered_json.read()

# create an empty dictionary to add all the filtered characters to by gender
filtered_dictionaryCHARAC_GEN= {}

for letter in filter_by_fic_character:
    for character in filter_by_fic_character[letter]:
# json file specifies per ontology/gender so filter for this in the filtered dictionary
        if "ontology/gender" in filter_by_fic_character[letter][character]:
            filtered_dictionaryCHARAC_GEN[character] =  filter_by_fic_character[letter][character]
# only want Male/Female for gender specification so split by /
            filtered_dictionaryCHARAC_GEN[character]["ontology/gender" ].split("/")
# only want last entry so reverse (Male/Female appears last in gender ontology)
            filtered_dictionaryCHARAC_GEN[character]["ontology/gender" ].reverse()
            filtered_dictionaryCHARAC_GEN[character]["ontology/gender" ] =  filtered_dictionaryCHARAC_GEN[character]["ontology/gender" ][0]

for character in filtered_dictionaryCHARAC_GEN:
    print(filtered_dictionaryCHARAC_GEN[character]["ontology/gender"])
# not all characters have a start year for the series/movie --> use external dataset to obtain information
# external dataset from Imdb for startyear of item (tsv file)
with open('title.basics.tsv') as file:         
    for character in filtered_dictionaryCHARAC_GEN:
        for line in file:
# if the name is the same for line in the imdb dataset to the name of item in DBpeople file, add the start year for the item to the dictionary made for the fictional characters
            if line.split('\t')[2] == filtered_dictionaryCHARAC_GEN[character]['ontology/firstAppearance']:
                filtered_dictionaryCHARAC_GEN[character]['start_year'] = line[5]

