def sentence_maker(phrases):
    capitalized = phrases.capitalize()
    interrogatives = ("How" , "What" , "When" , "Where" , "Why")
    if capitalized.startswith(interrogatives):
        return "%s?" % capitalized
    else:
        return "%s." % capitalized

SaySomethingElse = ""
while True:
    SaySomething = input("Say Something:")
    
    
    if SaySomething == "/end":
        break
    else: 
        SaySomethingElse = SaySomethingElse + " " + sentence_maker(SaySomething)
        continue
    
    
print(SaySomethingElse)