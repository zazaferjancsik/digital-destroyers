import json
characters = ['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M','N', 'P', 'Q', 'R', 'S','T', 'U', 'O', 'V', 'W', 'X', 'Y', 'Z']
#for character in characters:
    #with open(f'People/{character}_people.json',encoding='utf-8')as file:
        #contents = file.read()
character = []

for alphabet in characters:
    with open(f'People/{alphabet}_people.json',encoding='utf-8')as file:
        contents = json.load(file)
    for content in contents:
            if "http://www.w3.org/1999/02/22-rdf-syntax-ns#type_label" in content:
                for list in content["http://www.w3.org/1999/02/22-rdf-syntax-ns#type_label"]:
                        if 'fictional character'in list:
                            character.append(content)
    # print("Alphabet " +str(alphabet)+" done.")


with open('filtered_characters.json','w',encoding='utf-8')as file:
    json.dump(character,file, indent = 4)

# print("Done")




#Aborted attempt to use top 100 most common first names to find more data on gender




# with open('boys-names-txt.txt.txt', encoding = 'utf-8') as file_boys:
#     boys_names= file_boys.read()
# with open('girls-names-txt.txt.txt', encoding = 'utf-8') as file_girls:
#     girls_names=file_girls.read()
#     unique_girls_names = set()
#     unique_boys_names = set()
   
#     boys_names_list = boys_names.split("\t")
#     girls_names_list = girls_names.split("\t")

#     for name in girls_names_list:
#         if name not in unique_girls_names:
#             unique_girls_names.add(name)
#         else:
#             None
#     for nameB in boys_names_list:
#         if nameB not in unique_boys_names:
#             unique_boys_names.add(nameB)
#         else:
#             None
#     print(unique_boys_names)



    

# if title      name = character_dictionary['title'].split('_') only first so [0]
    # key for gender, and be value male
# if title split by _ first so [0]
# key for gender, and be value female

# line in boys_names / girls_names by semicolon,
# get script for unique words
