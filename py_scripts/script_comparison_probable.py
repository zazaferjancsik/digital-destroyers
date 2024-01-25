# import json to be able to 'probable_comparison.json'
import json

with open('probable_comparison.json', encoding='utf-8') as probable_json:
    filtered_and_probable= json.load(probable_json)

# set counts as 0 for total, good, and faulty counts --> counts = accurate by pronouns, faulty_counts = inaccurate by pronouns
    faulty_counts = 0
    counts = 0
    total_count = 0
# loop through the characters in the character json file 
    for character in filtered_and_probable:
# is the key 'probable gender' is present in a character dictionary, ...
        if 'probable gender' in filtered_and_probable[character]:
# add a count to the total count
            total_count += 1
# if the assigned gender by Wikipedia is the same as the probable gender, add a count to accuracy --> counts 
            if filtered_and_probable[character]["ontology/gender"] == filtered_and_probable[character]['probable gender']:
                counts += 1
# if the assigned gender by Wikipedia is NOT the same as the probable gender, add a count to not accuracy --> faulty_counts
            if filtered_and_probable[character]['ontology/gender'] != filtered_and_probable[character]['probable gender']:
                faulty_counts += 1
    print(total_count, counts, faulty_counts)

# get percentages for accuracy of the pronouns method:
    percentage_faulty = (faulty_counts/total_count)*100
    percentage_good = (counts/total_count)*100
    print(percentage_faulty)
    print(percentage_good)
# percentage_good is used as measure of accuracy/validity of pronouns method
