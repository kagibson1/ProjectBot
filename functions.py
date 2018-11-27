import requests
import json
import time
import datetime 
from datetime import date
import random

def findDate():
    return datetime.datetime.today().strftime('%A')
    
    
giphyAccessToken= "Bt45Xg33Kwyg1AhEqi0QO3YRNI8rJmZp"
wolframAccess = "GHU8TR-7XG3EWX29T"

def getRADonner():
    if findDate() == "Monday":
        return "Makayla"
    elif findDate() == "Tuesday":
        return "Hannah"
    elif findDate() ==  "Wednesday":
        return "Quincy"
    elif findDate() == "Thursday":
        return "Kumail"
    elif findDate() == "Friday":
        return "Jason"
    elif findDate() == "Saturday":
        return "Matt"
    elif findDate() == "Sunday":
        return "Kat"

# def whatsOpen():
#     if findDate() == "Monday":
#         
#     elif findDate() == "Tuesday":
#         return "Hannah"
#     elif findDate() ==  "Wednesday":
#         return "Quincy"
#     elif findDate() == "Thursday":
#         return "Kumail"
#     elif findDate() == "Friday":
#         return "Jason"
#     elif findDate() == "Saturday":
#         return "Matt"
#     elif findDate() == "Sunday":
#         return "Kat"
    
    


#from conversation with Jacob Strieb 
def getWeather():
    url= "https://wttr.in/Pittsburgh?0T&lang=en"
    r = requests.get(url)
    return r.text

def getAnswer(msg):
    url= "http://api.wolframalpha.com/v1/result?appid=GHU8TR-7XG3EWX29T" + "&i=" + msg
    r = requests.get(url)
    return r.text
    
def sayHello():
    return random.choice(["Hello", "How are you", "Hey hey"])

def checkForGreeting(text):
    greetingWords = ['hey', 'hi', 'hello']
    for i in greetingWords:
        if i in text:
            return(sayHello())
            
def checkForQuestion(text):
    questionWords = ["who", "what", "where", "when", "why", "how"]
    for i in questionWords:
        if i in text:
            return("You asked a question hehe let me think and give me a sec")
            
def getCatFact():
    url = "https://catfact.ninja/fact"
    r = requests.get(url)
    return(r.json()["fact"])

#from Jacob Strieb 
def getJoke():
    headers = { "Accept" : "application/json" }
    r = requests.get("https://icanhazdadjoke.com", headers=headers)
    return(r.json()["joke"])

def checkForTermination(text):
    terminationWords = ['bye', 'quit', 'end', 'see you later']
    for i in terminationWords:
        if i in text:
            return "Bye!"

#bad words we don't want chatbot responding to, list from https://github.com/dariusk/wordfilter
filter_words = set([ "ass", "fucking", "beeyotch", "biatch", "bitch", "chinaman", "chinamen", "fuck", "dickwad", "dumbass", 
    "chink", "crazie", "crazy", "crip", "cunt", "dago", "daygo", "dego", "dick",
    "dumb", "douchebag", "dyke", "fag", "fatass", "fatso", "gash", "gimp",
    "golliwog", "gook", "gyp", "halfbreed", "half-breed", "homo", "hooker",
    "idiot", "insane", "insanitie", "insanity", "jap", "kike", "kraut", 
    "lardass", "lesbo", "lunatic","negro", "nigga", "nigger", "nigguh",
    "paki", "pickaninnie", "pickaninny", "pussie", "pussy", "raghead",
    "retard", "shemale", "skank", "slut", "spade", "spic", "spook", "tard",
    "tits", "titt", "trannie", "tranny", "twat", "wetback", "whore", "wop"])

def checkForBadWords(text):
    for words in filter_words:
        if words in text:
            return ("I am sorry but this chatbot does not support profanity, please send another message but with kindness thanks")