import requests
import json
import random
from functions import *
from nlpWork import *
from food import *
import time


#tp2 timesheet
#tuesday nov 20 -- 4
#wednesday nov 21 -- 1
#thursday nov 22 -- 0
#friday nov 23 -- 4
#saturday nov 24 -- 1
#sunday nov 25 -- 3
#monday nov 26 -- 5 
#tuesday nov 27 -- 5
#wednesday nov 28 -- 2


accessToken= "f3zM1Gv02ML0AkBDYE5HRIViBuTqct5IoynHIrDL"
groupId = "46083099"

#the following functions above the **** were taken from https://jstrieb.github.io/chatbots/

def send(text):
    data = {"bot_id" : "6d75eacf991926065ef00ee35d", "text": text}
    requests.post("https://api.groupme.com/v3/bots/post", data = data)

def doHandshake():
    obj = [
        {
            "channel":"/meta/handshake",
            "version":"1.0",
            "supportedConnectionTypes":["long-polling"],
            "id":"1"
        }
    ]
    resp = requests.post("https://push.groupme.com/faye", json = obj)
    respObj = resp.json()
    return respObj[0].get("clientId")
    
# Get my user ID for later API calls
def getUserId(accessToken):
    data = { "access_token" : accessToken }
    r = requests.get("https://api.groupme.com/v3/users/me", params=data)
    return r.json()["response"]["user_id"]
    
def subscribeToChannel(clientId):
    userId = getUserId(accessToken)
    timestamp = time.time()
    obj = [
    {
    "channel":"/meta/subscribe",
    "clientId": clientId,
    "subscription":"/user/" + userId,
    "id":"2",
    "ext":
      {
        "access_token": accessToken,
        "timestamp": timestamp
      }
    }
    ]
    resp = requests.post("https://push.groupme.com/faye", json = obj)
    respObj = resp.json()

# Get new messages from the server
def getNew(clientId, numCalls):
    # Copied data from tutorial here: https://dev.groupme.com/tutorials/push
    data = [ {
               "channel" : "/meta/connect",
               "clientId" : clientId,
               "connectionType" : "in-process",
               "id" : "%d" % numCalls
             } ]
    try:
        r = requests.post("https://push.groupme.com/faye", json=data, stream=True)
    except:
        print("There was a problem getting the next messages.")
        return
    for line in r.iter_lines():
        preProcess(line.decode("utf-8"))
        
def preProcess(line):
    data = json.loads(line)
    for response in data:
        if "data" not in response: continue
        if "type" not in response["data"]: continue
        if response["data"]["type"] != "line.create": continue 
        if "subject" not in response["data"]: continue 
        
        msg = response["data"]["subject"]
        if msg["group_id"] != groupId: continue
        if msg["sender_type"] == "bot": continue
        
        process(msg)
#****************


def process(msg):
    answered = False 
    restyCheck = msg["text"]
    text = msg["text"].lower()
    
    #makes sure we avoid profanity
    if checkForBadWords(text) != None:
        answered = True
        send(checkForBadWords(text))
    
    #check for keywords in message
    if checkForGreeting(text) != None:
        answered = True 
        send(checkForGreeting(text))
        
    #I love Schatz...I want to do more with positive/negative words for TP3 so this was a start 
    if "schatz" in text and "is" in text:
        positiveWords= set(["good", "awesome", "tasty", "fantastic", "wonderful", "fun", "love"])
        negativeWords= set(["terrible", "bad", "gross", "hate"])
        for words in text.split(" "): 
            if words in positiveWords:
                print(words in positiveWords)
                send("Schatz is fantastic my friend")
            if words in negativeWords:
                answered = True
                send("Sir, I will have to disagree on this one")
                
    
    #sends message of name of who is on duty right now -- it's hardcoded for now by date
    if ("ra" or "resident assistant") and ("on duty" or "right now") in text:
        answered = True
        send("The RA on duty right now in Donner is " + getRADonner())
    
    #returns current *PITTSBURGH* weather 
    if "weather" in text:
        answered = True 
        send(getWeather())
    
    #tells you a terrible joke
    if "joke" in text:
        answered = True
        send("Here's a bad joke!\n" + getJoke())
    
    #sends random cat fact
    if "cat" and "fact" in text:
        answered = True
        send("Here's a cat fact!\n'" + getCatFact())
    
    #sends time closed of restaurant inputted / restuarant that it would autcorrect to if close
    if ("time" in text) and ("close" in text) and checkForRestaurants(restyCheck) != None:
        answered = True 
        restaurant = checkForRestaurants(restyCheck)
        closingTime = whatTimeDoesThisPlaceClose(restaurant)
        if len(closingTime) > 1:
            send(restaurant + " closes at " + closingTime[0] + " and " + closingTime[1])
        else: send(restaurant + " closes at " + closingTime[0])
    
    #sends time open of restaurant inputted / restaurant that it would autcorrect to if close
    if ("time" in text) and ("open" in text) and checkForRestaurants(restyCheck) != None:
        answered = True 
        restaurant = checkForRestaurants(restyCheck)
        openingTime = whatTimeDoesThisPlaceOpen(restaurant)
        if len(openingTime) > 1:
            send(restaurant + " opens at " + openingTime[0] + " and " + openingTime[1])
        else: send(restaurant + " opens at " + openingTime[0])
    
    #sends whether or not the restaurant / restaurant it would autocorrect to if close is currently open
    if "is" in text and "open" in text and checkForRestaurants(restyCheck) != None:
        answered = True
        restaurant = checkForRestaurants(restyCheck)
        if isThisPlaceOpen(restaurant) == True:
            send("Yeah! " + restaurant + " is open right now")
        else: send("Sorry bud try another restaurant because " + restaurant + " is closed right now" )
     
    #sends a formatted list of the restaurants that are open on campus right now    
    if answered == False and ("food" or "restaurants") and ("open" or "now") in text:
        answered = True 
        answer = " "
        open = list(whatsOpenRightNow())
        for elem in range(len(open)-1):
            answer += open[elem] + ", "
        answer += open[-1]
        send("These are the locations on campus that are open right now:" + answer)

#**********************set all personalized questions and answers above here
     
    #if we can't answer a question, then bop it to Wolfram Alpha so we don't look dumb 
    if answered == False and checkForQuestion(text) != None:
        answered = True 
        send(getAnswer(text)) 
        
    #check to see if a user wants to end the conversation 
    if checkForTermination(text) != None:
        answered = True 
        send(checkForTermination(text))
    
    #finally, if there's not a response yet, construct a response 
    if answered == False:
        send(actuallyRespond(text))
    
#****************

if __name__ == "__main__":
    clientId = doHandshake()
    subscribeToChannel(clientId)
    numCalls = 3
    while True:
        getNew(clientId, numCalls)
        numCalls += 1
    