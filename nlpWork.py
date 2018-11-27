import random
import os 
import nltk 


#functions based off of Liza Daly's tutorial "Chatbot Fundamentals: An Interactive Guide to Writing Bots in Python"
#and using nltk.org
def constructResponse(pronoun, noun, verb):
    response = [] 
    #to be able to see while testing 
    print("response = ", response)
    print("pronoun =", pronoun) 
    print("noun = ", noun)
    print("verb =", verb) 
    
    #make sure not to append None
    if pronoun != None: 
        response.append(pronoun)
        
    #adds verb and noun to form whole sentence now 
    if verb != None:
        verbWord = verb[0]
        print(verbWord)
        if verbWord in ("b", "am", "is", "'m" ):
            if pronoun.lower() == "you":
                response.append("are actually")
                if noun != None:
                    if startsWithVowel(noun):
                        articles = "an" 
                    else:
                        articles = "a"
                    response.append(articles + " " + noun)
                
        else:
            print(verbWord)
            response.append(verbWord)
            
            if noun != None:
                if startsWithVowel(noun):
                    articles = "an" 
                else:
                    articles = "a"
                response.append(articles + " " + noun)
                print(response)
    return " ".join(response)

def handlePronounsWeird(msg): #makes sure that it recognizes i as a pronoun 
    edited = []
    unedited = msg.split(' ')
    for word in unedited:
        if word == "i":
            word = "I"
        if word =="i'm":
            word = "I'm"
        edited.append(word)
        print(edited)
    return ' '.join(edited)

def startsWithVowel(word):
    if word[0] in "aeiou":
        return True
    else:
        return False 

def tokenizeAndTag(msg): 
    tokens = nltk.word_tokenize(msg)
    pos = nltk.pos_tag(tokens)
    return pos 


def choosePronoun(msg):#switches pronouns from You to I vice versa as suggested by tutorial
    pronoun = None
    for word, partOfSpeech in tokenizeAndTag(msg):
        if partOfSpeech == "PRP" and word.lower() == "you":
            pronoun = "I"
        elif partOfSpeech == "PRP" and word.lower() == "i":
            pronoun = "You"
    return pronoun

def chooseVerb(msg):#looks for VB (verb), guided by tutorial
    verb = None
    pos = None
    for word, partOfSpeech in tokenizeAndTag(msg):
        if partOfSpeech.startswith("VB"):
            verb = word
            pos = partOfSpeech
            break 
    return verb, pos
    
def chooseNoun(msg): #guided by tutorial
    noun = None
    for word, partOfSpeech in tokenizeAndTag(msg):
        if partOfSpeech == "NN":
            noun = word
            break
    return noun
    
def chooseAdjective(msg): #guided by tutorial
    adjective = None
    for word, partOfSpeech in tokenizeAndTag(msg):
        if partOfSpeech == "JJ":
            adjective = word
            break
    return adjective

def findPOS(msg): 
    print(msg)
    pronoun = choosePronoun(msg)
    verb = chooseVerb(msg)
    adjective = chooseAdjective(msg)
    noun = chooseNoun(msg)
    return (pronoun, verb, adjective, noun)
    
def actuallyRespond(msg):
    cleaned = handlePronounsWeird(msg)
    pronoun = findPOS(cleaned)[0]
    noun = findPOS(cleaned)[3]
    adjective = findPOS(cleaned)[2]
    verb = findPOS(cleaned)[1]
    print(verb)
    response = None     
    if pronoun == None:
        response = "I agree totally!"
    elif pronoun == "I" and verb == None:
        response == "I'm pretty cool, right? This is a hard project, my dude."
    else:
        response = constructResponse(pronoun, noun, verb)
    if response == None:
        return "sorry mate I don't know what you're saying since ya got thru this"
    return response 

##Test it here 
#text='I like orange'
#respond = actuallyRespond(text)
#print(respond)    

