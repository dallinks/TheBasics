## imports 
import json
from difflib import get_close_matches

## variables
while True:
    data = json.load(open("data.json"))
    userinput = input("Enter a word: ")
    matchedword = get_close_matches(userinput,data.keys())

    def MakeLowercase(word):
        return word.lower()

    def translate(code):
        code = code.lower()
        if code in data:
            return data[code]
        elif code.title() in data:
            return data[code.title()]
        elif code.upper() in data:
            return data[code.upper()]
        elif matchedword == []:
            return "That's  not a word..."
        elif matchedword != []:
            firstYN = input("Did you mean %s? input Y or N: " % matchedword[0])
            if firstYN == "Y":
                return data[str(matchedword[0])]
            elif firstYN == "N":
                SecondYN = input("Did you mean %s? input Y or N: " % matchedword[1])
                if SecondYN == "Y":
                    return data[str(matchedword[1])]
                elif SecondYN == "N": 
                    ThirdYN = input("Did you mean %s? input Y or N: " % matchedword[2])
                    if ThirdYN == "Y":
                        return data[str(matchedword[2])]
                    else:
                        return "Your word is not in our database"
                else:
                    return "We didn't understand your entry"
            else: 
                return "We didn't understand your entry"
        else:
            return "The word doesn't exist. Please double-check it." 
    print(translate(userinput))







