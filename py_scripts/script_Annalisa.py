#import and open to read json file (DBpeople filtered for fictional characters)

import re
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
    

                # filtered_dictionary_CHARAC_GEN_FOR_CSV['gender'] = filtered_dictionaryCHARAC_GEN[letter['ontology/gender']]
# only want last entry so reverse (Male/Female appears last in gender ontology)
       
# not all characters have a start year for the series/movie --> use external dataset to obtain information
# external dataset from Imdb for startyear of item (tsv file)

#dictionary for titles we have to find in the imdb dataset
start_year_dictionary = {}
#list of common misleadin first appearances
misleadingfirstappearance = ['Television', 'Pilot', 'Series', 'Movie', 'Miniseries', 'Pilot episode', 'TV Series', 'Television:']

#filtering out the characters for start year criteria
for character in filtered_dictionaryCHARAC_GEN:
    #making sure the character has label ontology/firstappearance
    if 'ontology/firstAppearance' in filtered_dictionaryCHARAC_GEN[character]:    
        #if first appearance has a list it has to be handled differently
        if type(filtered_dictionaryCHARAC_GEN[character]['ontology/firstAppearance']) == list:
            #looping through all elements in the list
            for appearance in filtered_dictionaryCHARAC_GEN[character]['ontology/firstAppearance']:
                #if any contains a year, it will be assigned as first appearance
                matches  = re.search('[12][0-9]{3}', appearance)
                if matches is not None:
                    filtered_dictionaryCHARAC_GEN[character]['start_year'] = matches.group(0)
                    break
            #if there was no start year assigned, it will put its title in a dictionary, unless its a misleading first appearance
            if 'start_year' not in filtered_dictionaryCHARAC_GEN[character]:
                for appearance in filtered_dictionaryCHARAC_GEN[character]['ontology/firstAppearance']:
                    if appearance not in misleadingfirstappearance:
                        start_year_dictionary[appearance] = {}
                        start_year_dictionary[appearance]['title'] = character
                        #if it is put into the start year dictionary, it also assigns the start year 3000, which will be explained later
                        filtered_dictionaryCHARAC_GEN[character]['start_year'] = 3000
                        break
        else:
            #if its not a list, it does the same thing except the loops
            matches  = re.search('[12][0-9]{3}', filtered_dictionaryCHARAC_GEN[character]['ontology/firstAppearance'])
            if matches is not None:
                filtered_dictionaryCHARAC_GEN[character]['star_year'] = matches.group(0)
            else:
                if filtered_dictionaryCHARAC_GEN[character]['ontology/firstAppearance'] not in misleadingfirstappearance:
                    start_year_dictionary[filtered_dictionaryCHARAC_GEN[character]['ontology/firstAppearance']] = {}
                    start_year_dictionary[filtered_dictionaryCHARAC_GEN[character]['ontology/firstAppearance']]['title'] = character
                    filtered_dictionaryCHARAC_GEN[character]['start_year'] = 3000

#opens the imdb dataset line by line
#checks if the title in the imdb dataset is in our start year dictionary
#if match found it will check if the start year is smaller then the already existing one, and only assigns it, if it is
#this is why we assigned 3000, so there is a starting value, which is definitely larger
count = 0
with open('title.basics.tsv') as file:         
    for line in file:
        if line.split('\t')[2] in start_year_dictionary:
            #some values are missing in the imdb dataset, that we have to filter for
            if line.split('\t')[5] != '\\N':
                if int(line.split('\t')[5]) < int(filtered_dictionaryCHARAC_GEN[start_year_dictionary[line.split('\t')[2]]['title']]['start_year']):
                    filtered_dictionaryCHARAC_GEN[start_year_dictionary[line.split('\t')[2]]['title']]['start_year'] = int(line.split('\t')[5])
                    #the print helps us keep track of progress, as it has to go through around 10,000,000 lines
                    print("Done for "+str(start_year_dictionary[line.split('\t')[2]]['title'])+ 'year: '+  str(line.split('\t')[5])+" line: "+ str(count))
        count += 1

#changes any values that were unmatched to NA
for character in filtered_dictionaryCHARAC_GEN:
    if 'ontology/firstAppearance' in filtered_dictionaryCHARAC_GEN[character]:    
        if filtered_dictionaryCHARAC_GEN[character]['start_year'] == 3000:
            filtered_dictionaryCHARAC_GEN[character]['start_year'] = 'NA'
print(count)

#creates a dictionary for the csv only containng the releveant information
for character in filtered_dictionaryCHARAC_GEN:
    if 'ontology/firstAppearance' in filtered_dictionaryCHARAC_GEN[character]:
        filtered_dictionary_CHARAC_GEN_FOR_CSV.append({
            'fic_character': filtered_dictionaryCHARAC_GEN[character]['title'],
            'gender' : filtered_dictionaryCHARAC_GEN[character]['ontology/gender'],
            'start_year': filtered_dictionaryCHARAC_GEN[character]['start_year']
        })
import csv

#writes the dictionary into a CSV file
with open('dictionary_fictional_characters_gender.csv', 'w', newline='') as file:
    fieldnames = ['fic_character', 'gender', 'start_year']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    for item in filtered_dictionary_CHARAC_GEN_FOR_CSV:
        writer.writerow(item)

