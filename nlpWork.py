import random
import os 
from textblob import TextBlob
import nltk 


def constructResponse(pronoun, noun, verb):

    response = []
    
    print("response = ", response)
    print("pronoun =", pronoun) 
    print("noun = ", noun)
    print("verb =", verb) 
    
    if pronoun != None: 
        response.append(pronoun)
    
    if verb != None:
        verbWord = verb[0]
        if verbWord in ("b", "am", "is", "'m" ):
            if pronoun.lower() == "you":
                response.append("are really")
            else:
                response.append(verbWord)
    
    if noun != None:
        if startsWithVowel(noun):
            pronoun = "an" 
        else:
            pronoun = "a"
        response.append(pronoun + " " + noun)
    
    return " ".join(response)

def handlePronounsWeird(msg):
    edited = []
    unedited = msg.split(' ')
    for word in unedited:
        if word == "i":
            word = "I"
        if word =="i'm":
            word = "I'm"
        edited.append(word)
    return ' '.join(edited)

def startsWithVowel(word):
    if word[0] in "aeiou":
        return True
    else:
        return False 

def tokenizeAndTag(msg):#guidance from nltk website 
    tokens = nltk.word_tokenize(msg)
    pos = nltk.pos_tag(tokens)
    return pos 


def choosePronoun(msg):
    pronoun = None
    for word, partOfSpeech in tokenizeAndTag(msg):
        if partOfSpeech == "PRP" and word.lower() == "you":
            pronoun = "I"
        elif partOfSpeech == "PRP" and word.lower() == "i":
            pronoun = "You"
    return pronoun

def chooseVerb(msg):
    verb = None
    pos = None
    for word, partOfSpeech in tokenizeAndTag(msg):
        if partOfSpeech.startswith("VB"):
            verb = word
            pos = partOfSpeech
            break 
    return verb, pos
    
def chooseNoun(msg):
    noun = None
    for word, partOfSpeech in tokenizeAndTag(msg):
        if partOfSpeech == "NN":
            noun = word
            break
    return noun
    
def chooseAdjective(msg):
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
    response = None 
    
    
    if pronoun == None:
        response = "I agree totally!"
    elif pronoun == "I" and verb == None:
        response == "I'm pretty cool aren't I?"
    else:
        response = constructResponse(pronoun, noun, verb)
    if response == None:
        return "sorry mate I don't know what you're saying since ya got thru this"
    return response 
    

            

            
    
    