import requests
import json
import time
import random
from functions import *
from nlpWork import *
import datetime 

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
    text = msg["text"].lower()
    
    if checkForBadWords(text) != None:
        answered = True
        send(checkForBadWords(text))
    
    if checkForGreeting(text) != None:
        answered = True 
        send(checkForGreeting(text))
    # 
    # if ("RA" or "resident assistant") and ("on duty" or "right now") in text:
    #     answered = True
    #     send(getRADonner())
    #     
        
        
    if "weather" in text:
        answered = True 
        send(getWeather())
        
    if "joke" in text:
        answered = True
        send("Here's a bad joke!\n" + getJoke())
        
    if "cat" and "fact" in text:
        answered = True
        send("Here's a cat fact!\n'" + getCatFact())

#**********************set all personalized questions and answers above here
        
    if checkForQuestion(text) != None:
        answered = True 
        send(getAnswer(text)) 
        
        
    if checkForTermination(text) != None:
        answered = True 
        send(checkForTermination(text))
    
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
    