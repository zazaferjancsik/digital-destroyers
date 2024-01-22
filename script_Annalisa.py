import json

with open() as filtered_json:
    filter_by_fic_character = filtered_json.read()

for letter in filter_by_fic_character:
    for character in filter_by_fic_character[letter]:
        if filter_by_fic_character[letter][character][ontology/gender]