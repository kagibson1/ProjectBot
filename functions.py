import requests
import json
import time
import random

giphyAccessToken= "Bt45Xg33Kwyg1AhEqi0QO3YRNI8rJmZp"

#from conversation with Jacob Strieb 
def getWeather():
    url= "https://wttr.in/Pittsburgh?0T&lang=en"
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
    