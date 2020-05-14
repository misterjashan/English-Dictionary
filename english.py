import json
from difflib import get_close_matches


data = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s instead? If Yes then enter Y if No then enter N " % get_close_matches(w, data.keys())[0])
        
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N":
            return "this word dosen't exist."
        else:
            return "Sorry we did not understand your request"
    else:
        return "This word dosen't exist."    

word = input("Enter the word:  ")

output = translate(word)

if type(output) == list:
    for items in output:
        print(items)
else:
    print(output)