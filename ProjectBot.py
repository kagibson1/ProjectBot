import requests
import json
import random
from functions import *
from nlpWork import *
from food import *
import time


#tp3 timesheet
#sunday dec 2: 1:30 pm - 2:30 pm 
#monday dec 3: 4:30 Am - 6 am, 12:00-1:30 pm, 7:30-8:15 pm, 10:00-11:30 pm
#tuesday dec 4: 10:30 am - 12:00 pm 
#wednesday dec 5:
#ahhhhh thursday dec 6:

prevMess = {"what the fudge": "WAYOOOOOOO"}
lastMessage = ""

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
    global lastMessage
    print(prevMess)
    answered = False 
    restyCheck = msg["text"]
    text = msg["text"].lower() 
    print(text)
    print(text in prevMess)
    
    #fix the input if there's a change to be made 
    isChange = fixInput(text, prevMess, lastMessage)
    
    if isChange != None and answered == False:
        answered = True 
        send(isChange)
        
    #speeds it up!
    if text in prevMess and answered == False: 
        answered = True 
        lastMessage = prevMess[text]
        send( prevMess[text] )  
    
    #makes sure we avoid profanity
    if checkForBadWords(text) != None and answered == False:
        answered = True
        send(checkForBadWords(text))
    
    #check for keywords in message
    if checkForGreeting(text) != None and answered == False:
        answered = True 
        send(checkForGreeting(text))
        
    if checkForAboutMe(text) != None and answered == False:
        answered = True 
        send(checkForAboutMe(text))
        
    checkCourseStuff = appropCourseResponse(text)
    if checkCourseStuff != None:
        answered = True
        send(checkCourseStuff)
    
        
    #swim team <3s schatz
    if "schatz" in text and "is" in text and answered == False:
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
    if ("ra" or "resident assistant") and ("on duty" or "right now") in text and answered == False:
        answered = True
        send("The RA on duty right now in Donner is " + getRADonner())
    
    #returns current *PITTSBURGH* weather 
    if "weather" in text and answered == False:
        answered = True 
        send(getWeather())
    
    #tells you a terrible joke
    if "joke" in text and answered == False:
        answered = True
        send("Here's a bad joke!\n" + getJoke())
    
    #sends random cat fact
    if "cat" and "fact" in text and answered == False:
        answered = True
        send("Here's a cat fact!\n'" + getCatFact())
        

    if answered == False and ("time" in text or "open" in text) and ("food" not in text and "restaurants" not in text):
        findRest = checkForRestaurants(restyCheck)
    
    #sends time closed of restaurant inputted / restuarant that it would autcorrect to if close
    if answered == False and ("time" in text) and ("close" in text) and findRest != None:
        answered = True 
        restaurant = findRest
        closingTime = whatTimeDoesThisPlaceClose(restaurant)
        if len(closingTime) > 1:
            response = restaurant + " closes at " + closingTime[0] + " and " + closingTime[1]
            prevMess[text] = response
            lastMessage = text
            send(response)
        else: 
            response = restaurant + " closes at " + closingTime[0]
            prevMess[text] = response
            lastMessage = text
            send(response)
    
    #sends time open of restaurant inputted / restaurant that it would autcorrect to if close
    if answered == False and ("time" in text) and ("open" in text) and findRest != None:
        answered = True 
        restaurant = findRest
        openingTime = whatTimeDoesThisPlaceOpen(restaurant)
        if len(openingTime) > 1:
            response = restaurant + " opens at " + openingTime[0] + " and " + openingTime[1]
            prevMess[text] = response
            lastMessage = text
            send(response)
        else: 
            response = restaurant + " opens at " + openingTime[0]
            prevMess[text] = response
            lastMessage = text
            send(response)
    
    #sends whether or not the restaurant / restaurant it would autocorrect to if close is currently open
    if answered == False and "is" in text and "open" in text and findRest != None:
        answered = True
        restaurant = findRest
        if isThisPlaceOpen(restaurant) == True:
            response = "Yeah! " + restaurant + " is open right now"
            prevMess[text] = response
            lastMessage = text
            send(response)
        else: 
            response = "Sorry bud try another restaurant because " + restaurant + " is closed right now" 
            prevMess[text] = response
            lastMessage = text
            send(response)
     
    #sends a formatted list of the restaurants that are open on campus right now    
    if answered == False and ("food" in text or "restaurants" in text) and ("open" in text or "now" in text):
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
        response = actuallyRespond(text)
        prevMess[text] = response
        lastMessage = text
        send(response)
        
    print(prevMess)
    
#****************

if __name__ == "__main__":
    clientId = doHandshake()
    subscribeToChannel(clientId)
    numCalls = 3
    while True:
        getNew(clientId, numCalls)
        numCalls += 1