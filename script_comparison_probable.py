import json

with open('probable_comparison.json', encoding='utf-8') as probable_json:
    filtered_and_probable= json.load(probable_json)

    faulty_counts = 0
    counts = 0
    total_count = 0
    for character in filtered_and_probable:
        if 'probable gender' in character:
            total_count += 1
            if character["ontology/gender"] == character['probable gender']:
                counts += 1
            if character['ontology/gender'] != character['probable gender']:
                faulty_counts += 1
    print(total_count, counts, faulty_counts)
