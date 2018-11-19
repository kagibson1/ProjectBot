import requests
import json
import time
import random

giphyAccessToken= "Bt45Xg33Kwyg1AhEqi0QO3YRNI8rJmZp"

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
            answered = True
            
def checkForQuestion(text):
    questionWords = ["who", "what", "where", "when", "why", "how"]
    for i in questionWords:
        if i in text:
            return("You asked a question hehe let me think and give me a sec")
            answered = True
            
#from jacob's link yay ill cite later            
def processGif():
    data = {
            "api_key" : giphyAccessToken,
            "q" : "cat",
            "offset" : random.randint(0, 500)
        }
    
    r = requests.get("http://api.giphy.com/v1/gifs/search", params=data)
    return r.text 
