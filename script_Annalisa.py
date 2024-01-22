import json

with open() as filtered_json:
    filter_by_fic_character = filtered_json.read()


filtered_dictionaryCHARAC_GEN= {}

for letter in filter_by_fic_character:
    for character in filter_by_fic_character[letter]:
        if "ontology/gender" in filter_by_fic_character[letter][character]:
            filtered_dictionaryCHARAC_GEN[character] =  filter_by_fic_character[letter][character]
            filtered_dictionaryCHARAC_GEN[character]["ontology/gender" ].split("/")
            filtered_dictionaryCHARAC_GEN[character]["ontology/gender" ].reverse()
            filtered_dictionaryCHARAC_GEN[character]["ontology/gender" ] =  filtered_dictionaryCHARAC_GEN[character]["ontology/gender" ][0]

for character in filtered_dictionaryCHARAC_GEN:
    print(filtered_dictionaryCHARAC_GEN[character]["ontology/gender"])

with open('title.basics.tsv') as file:          #opening csv file
    for character in filtered_dictionary:
        for line in file:
            if line.split('\t')[2] == filtered_dictionary[character]['ontology/firstAppearance']:
                filtered_dictionary[character]['start_year'] = line[5]

