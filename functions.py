import requests
import json
import time
import datetime 
from datetime import date
import random

#returns the current day of the week 
def findDate():
    return datetime.datetime.today().strftime('%A')


giphyAccessToken= "Bt45Xg33Kwyg1AhEqi0QO3YRNI8rJmZp"
wolframAccess = "GHU8TR-7XG3EWX29T"

#returns the RA on duty in Donner right now
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
        
def fixInput(text, prevMess, lastMessage):
    print("THIS IS TEXT" + text)
    if "‘" in text:
        weSplit = text.split("‘")
        print("we split", weSplit)
        if weSplit[0].strip() == "did you mean":
            value = weSplit[1][:-1]
            prevMess[lastMessage] = value[0].upper() + value[1:]
            return("Yeah I meant " +  weSplit[1][:-1])

#checks to see if text contains a restaurant name or if it contains something ish close to a restuarant name 
#need to tweak to make faster for long inputs (it does work it just isn't great ui)
def checkForRestaurants(text): #sos how do i make this faster for long names like Taste of India 
    restaurants= {"Au Bon Pain", "Bibimbap", "Bowl Life", "BYOB",
         "Create", "Cucina", "El Gallo", "Entropy", "Exchange",
         "Heinz Cafe", "Innovation","iNoodle", "Resnik Cafe",
         "Nakama", "Nourish", "Pomegranate",
        "La Prima", "Realwich", "Rohr Cafe", "Rooted", 
        "Schatz", "Seiber Cafe", "Stephanie's", "Underground", "Zebra Lounge"}
        #removed Black Bar Grill, Tartan Express, Gingers Express, Taste of India
    
    #works for 1 word restaurant names that are correctly spelled 
    for word in text.split(" "):
        if word in restaurants:
            return word 
    
    #find all possible strings with 3 words, 2 words, 1 word, add to set 
    potRest = set()
    for i in range(len(text.split(" "))-3):
        myStr = str(text.split(" ")[i]) + " " + str(text.split(" ")[i+1]) + " " + str(text.split(" ")[i+2])
        potRest.add(myStr)
    for j in range(len(text.split(" "))-2):
        myStr = str(text.split(" ")[j]) + " " + str(text.split(" ")[j+1])
        potRest.add(myStr)
    for k in range(len(text.split(" "))):
        myStr = str(text.split(" ")[k])
        potRest.add(myStr)
    
    minNumCh = None
    textWord = None
    actRest = None
    
    print(potRest, restaurants)
    #finds minimum number of changes to get restaurant name from input 
    for possible in potRest:
        for rest in restaurants:
            print(possible, rest)
            if len(rest) >=  (len(possible) + 3):
                continue 
            print(numChanges(possible, rest))
            if minNumCh == None or numChanges(possible, rest) < minNumCh:
                minNumCh = numChanges(possible, rest)
                textWord = possible
                actRest = rest
    print("yo we made it")
    if minNumCh <= len(actRest):
        return actRest 
    return None

#function that finds the minimum number of changes recursively with 2 base cases
#and 2 recursive calls depending on if your current aligning letters are the same     
def numChanges( s1, s2, i =0 ,j = 0):
    if i >= len(s1): #out of bounds, base case
        return max(0, len(s2) -i) #find num of letters left
    if j>= len(s2): #out of bounds, base case 
        return max(0, len(s1) -j) #num of letters left
    if s1[i] == s2[j]: 
        return numChanges(s1, s2, i+1, j+1) #move on and check the rest
    else: #find least number of changes, add 1 for each change
        return 1+min(numChanges(s1, s2, i+1,j), numChanges(s1, s2, i, j+1)) 


#from conversation with Jacob Strieb 
def getWeather():
    url= "https://wttr.in/Pittsburgh?0T&lang=en"
    r = requests.get(url)
    return r.text

#use wolfram alpha api to answer questions that we don't know the answers
def getAnswer(msg):
    url= "http://api.wolframalpha.com/v1/result?appid=GHU8TR-7XG3EWX29T" + "&i=" + msg
    r = requests.get(url)
    return r.text

#returns a random greeting
def sayHello():
    return random.choice(["Hello", "Hey!", "Hey hey"])

#checks for greeting in the text
def checkForGreeting(text):
    greetingWords = ['hey', 'hi', 'hello']
    for i in greetingWords:
        if i in text.split(" "):
            return(sayHello())

#checks for a question in the text
def checkForQuestion(text):
    questionWords = ["who", "what", "where", "when", "why", "how"]
    for i in questionWords:
        if i in text:
            return(i)

#returns a reandom cat fact from this website
def getCatFact():
    url = "https://catfact.ninja/fact"
    r = requests.get(url)
    print(r.json()["fact"])
    return(r.json()["fact"])

#from Jacob Strieb, returns random dad joke from website 
def getJoke():
    headers = { "Accept" : "application/json" }
    r = requests.get("https://icanhazdadjoke.com", headers=headers)
    return(r.json()["joke"])

#checks for words that would signal the user wants to end conversation 
def checkForTermination(text):
    terminationWords = set(['bye', 'quit', 'end', 'see you later'])
    for words in text.split(" "):
        if words in terminationWords:
            return "Bye!"
    

#bad words we don't want chatbot responding to, list from https://github.com/dariusk/wordfilter and then added what friends were putting into the bot yikes
filter_words = set([ "ass", "fucking", "beeyotch", "biatch", "bitch", "chinaman",    
    "chinamen", "fuck", "dickwad", "dumbass", "shit", "fuckeroni", "shithead", 
    "poopy", "crap", "fuq", "dipshit", "riptard", "dumbnut", "emmanuel", "ej"
    "chink", "crazie", "crazy", "cunt", "dago", "daygo", "dego", "dick",
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
            
def checkForAboutMe(msg):
    meInfo = {"name": "My name is ProjectBot", "age": "I am " + str(date.toordinal(date.today()) - date.toordinal(date(2018,11,16))) + " days old", "why": "I was made for the 15-112 Term Project!"  }
    
    if checkForQuestion(msg) != None and ("you" in msg or "your" in msg):
        if "name" in msg:
            return meInfo["name"]
        elif "old" in msg or "age" in msg:
            return meInfo["age"]
        if "created" in msg or "made" in msg:
            return meInfo["why"]

#from json documentation, cmu course data from scotty labs github (https://github.com/ScottyLabs/course-api)
data = json.loads(open("cmu_course_data.json", "r").read())

def isCourse(str): #checks to see if a certain string is in course format of XX-XXX
    digits = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    if len(str) == 7 and str[6] == "?":
        str = str[0:6]
    if (len(str) != 6):
        return None
    
    if (str[0] in digits and str[1] in digits and str[2] == "-" and str[3] in digits and str[4] in digits and str[5] in digits):
        return str 

#finds the course from the whole text
def findCourse(text): 
    for words in text.split(" "):
        if isCourse(words) != None:
            return isCourse(words)
 
#based on contents of input will return the correct course information
def appropCourseResponse(text):
    course = findCourse(text)
    if course not in data["courses"]:
        return None
    if "units" in text:
        return("The number of units of " + course + " is " + str(data["courses"][course]["units"]))
    if "prereqs" in text:
        prereqs =  data["courses"][course]["prereqs"]
        if prereqs == None:
            return ("The prereqs for " + course + " are nonexistent yeehaw!")
        if prereqs != None:
            return ("The prereqs for " + course + " are " + data["courses"][course]["prereqs"])
    if "coreqs" in text:
        coreqs =  data["courses"][course]["coreqs"]
        if coreqs == None:
            return ("The coreqs for " + course + " are nonexistent yeehaw!")
        if coreqs != None:
            return ("The coreqs for " + course + " are " + data["courses"][course]["coreqs"])
    if "description" in text:
        return ("Here is the course description for " + course + ": " + data["courses"][course]["desc"])
    
def extractKey(text, prevMess):
    if "remember that if i say " in text:
        first = text.split("remember that if i say ")
        print(first)
        second = first[1].split("you say ")
        print(second)
        key = second[0].strip()
        print(key)
        print(key == "kellen is awesome")
        value = second[1].strip()
        value = value[0].upper() + value[1:]
        print(value)
        prevMess[key] = value
        print(prevMess)
        return("Noted!")