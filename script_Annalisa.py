import json

with open() as filtered_json:
    filter_by_fic_character = filtered_json.read()


filtered_dictionaryCHARAC_GEN= {}

for letter in filter_by_fic_character:
    for character in filter_by_fic_character[letter]:
        if "ontology/gender" in filter_by_fic_character[letter][character]:
            filtered_dictionaryCHARAC_GEN[character] =  filter_by_fic_character[letter][character]
print()