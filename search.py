import json
import difflib

#loading json data onto the dictionary
with open('data.json', 'r') as file:
    data_dict=json.load(file)



def definition(word):
    if word in data_dict:
        explanation=data_dict[word]
        print(explanation)
    else:
        suggestions= difflib.get_close_matches(word, data_dict.keys(),n=3,cutoff=0.8)
        if suggestions:
            print(f'Definition not found. Did you mean one of these?')
            for suggestion in suggestions:
                print(f'- {suggestion}: {data_dict[suggestion]}')
        else:
            explanation='Search Results: \n Definition not found'
            print(explanation)

search_word=input('Enter a word to look up it definition: ')
search_word=search_word.lower()
definition(search_word)