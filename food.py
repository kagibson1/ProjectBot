import datetime 
from datetime import date

#read python documentation for datetime module 
#returns current day of week
def findDate():
    return datetime.datetime.today().strftime('%A')

#returns the current time in minutes past midnight
def currTimeMinutes():
    return int(datetime.datetime.today().strftime('%H'))*60 + int(datetime.datetime.today().strftime('%M'))

#returns what restaurants are open right now depending on the day of the week 
def whatsOpenRightNow():
    day = findDate()
    time = currTimeMinutes()
    print (time)
    open = set()
    if day == "Saturday":
        for i in range(len(restaurantsSaturdays)):
            for j in range(1, len(restaurantsSaturdays[i])):
                if time > restaurantsSaturdays[i][j][0] and time < restaurantsSaturdays[i][j][1]:
                    open.add(restaurantsSaturdays[i][0])
                    break 
    elif day == "Sunday":
        for i in range(len(restaurantsSundays)):
            for j in range(1, len(restaurantsSundays[i])):
                if time > restaurantsSundays[i][j][0] and time < restaurantsSundays[i][j][1]:
                    open.add(restaurantsSundays[i][0])
                    break 
    elif day == "Friday":
        for i in range(len(restaurantsFridays)):
            for j in range(1, len(restaurantsFridays[i])):
                if time > restaurantsFridays[i][j][0] and time < restaurantsFridays[i][j][1]:
                    open.add(restaurantsFridays[i][0])
                    break 
    else:    
        for i in range(len(restaurantsWeekdays)):
            for j in range(1, len(restaurantsWeekdays[i])):
                if time > restaurantsWeekdays[i][j][0] and time < restaurantsWeekdays[i][j][1]:
                    open.add(restaurantsWeekdays[i][0])
                    break 
    return open

#checks to see if a certain restaurant is open 
def isThisPlaceOpen(place):
    open = whatsOpenRightNow()
    if place in open:
        return True 
    return False

#returns the time that a restaurant opens depending on the day of week
def whatTimeDoesThisPlaceOpen(place):
    day = findDate()
    time = currTimeMinutes()
    print (time)
    openingTimeInMinutes = []
    if day == "Saturday":
        for i in range(len(restaurantsSaturdays)):
            if restaurantsSaturdays[i][0] == place:
                for j in range(1, len(restaurantsSaturdays[i])):
                    openingTimeInMinutes.append(restaurantsSaturdays[i][j][0])
                break
                
    elif day == "Sunday":
        for i in range(len(restaurantsSundays)):
            if restaurantsSundays[i][0] == place:
                for j in range(1, len(restaurantsSundays[i])):
                    openingTimeInMinutes.append(restaurantsSundays[i][j][0])
                break
    elif day == "Friday":
        for i in range(len(restaurantsFridays)):
            if restaurantsFridays[i][0] == place:
                for j in range(1, len(restaurantsFridays[i])):
                    openingTimeInMinutes.append(restaurantsFridays[i][j][0])
                break
    else:    
        for i in range(len(restaurantsWeekdays)):
            if restaurantsWeekdays[i][0] == place:
                for j in range(1, len(restaurantsWeekdays[i])):
                    openingTimeInMinutes.append(restaurantsWeekdays[i][j][0])
                break
    return formatTimesToNormal(openingTimeInMinutes)

#returns what time a restaurant closes depending on the day of the week
def whatTimeDoesThisPlaceClose(place):
    day = findDate()
    time = currTimeMinutes()
    print (time)
    closingTimeInMinutes = []
    if day == "Saturday":
        for i in range(len(restaurantsSaturdays)):
            if restaurantsSaturdays[i][0] == place:
                for j in range(1, len(restaurantsSaturdays[i])):
                    closingTimeInMinutes.append(restaurantsSaturdays[i][j][1])
                break
                
    elif day == "Sunday":
        for i in range(len(restaurantsSundays)):
            if restaurantsSundays[i][0] == place:
                for j in range(1, len(restaurantsSundays[i])):
                    closingTimeInMinutes.append(restaurantsSundays[i][j][1])
                break
    elif day == "Friday":
        for i in range(len(restaurantsFridays)):
            if restaurantsFridays[i][0] == place:
                for j in range(1, len(restaurantsFridays[i])):
                    closingTimeInMinutes.append(restaurantsFridays[i][j][1])
                break
    else:    
        for i in range(len(restaurantsWeekdays)):
            if restaurantsWeekdays[i][0] == place:
                for j in range(1, len(restaurantsWeekdays[i])):
                    closingTimeInMinutes.append(restaurantsWeekdays[i][j][1])
                break
    answer = formatTimesToNormal(closingTimeInMinutes)
    if "11:59 PM" in answer:
        answer.remove("11:59 PM")
    return answer

#cleans up our time by formatting to AM/PM and hour:minute
def formatTimesToNormal(lstTimes):
    normal = []
    timeOfDay = ""
    for i in range(len(lstTimes)):
        numHours = (lstTimes[i]) // 60
        if numHours > 12:
            numHours -= 12
            timeOfDay = "PM"
        else: timeOfDay = "AM"
        numMinutes = str(lstTimes[i] % 60)
        if numMinutes == "0":
            correctNum = "00"
        else: correctNum = numMinutes
        normal.append(str(numHours) + ":" + str(correctNum) + " " + timeOfDay)
    return normal 

#all dining information from cmu dining webpages, converted into number of minutes since midnight 
#had to be split into different days of the week since there are different times open on different days
#executive move to NOT list Schatz as open for lunch since it isn't open for undergrads and therefore not me and im all that matters 
#also considering not including "cafes" only since I would want to use this for actual food 
restaurantsWeekdays = [
["Au Bon Pain", (0,120), (420,1439)],
["BBG", (630, 1260)],
["Bibimbap",(630,1260)],
["Bowl Life", (630, 1260)],
["BYOB", (660, 870), (1020, 1260)],
["Resnik Cafe", (0,120), (420,1439)],
["Create", (630, 1260)],
["Cucina", (660, 1380)],
["El Gallo", (630,1320)],
["Entropy", (0,180), (450,1439)],
["Exchange", (480,1200)],
["Gingers Express", (480, 960)],
["Heinz Cafe", (510,1080)],
["Innovation", (660,870),(1020,1260)],
["iNoodle", (480,1200)],
["Nakama", (660, 870), (1020, 1260)],
["Nourish", (630, 1110)],
["Pomegranate", (660, 1260)],
["La Prima", (480,1080)],
["Realwich", (630, 960)],
["Rohr Cafe", (420,1140)],
["Pure", (420, 1260)],
["Rooted", (630, 1260)],
["Schatz", (450,630),(1020,1260)],
["Seiber Cafe", (450, 900)],
["Stephanie's", (0,1439)],
["Tartan Express", (660, 1170)],
["Taste of India", (660, 840), (1020, 1260)],
["Underground", (0, 120), (510, 1439)],
["Zebra Lounge", (480, 1020)]]

restaurantsFridays = [
["Au Bon Pain", (0,120), (420,1439)],
["BBG", (630, 1260)],
["Bibimbap", (630,1260)],
["Bowl Life", (630, 1260)],
["BYOB", (660, 870), (1020, 1260)],
["Resnik Cafe", (0,120), (420,1439)],
["Create", (630, 1260)],
["Cucina", (660, 1380)],
["El Gallo", (630,1320)],
["Entropy", (0,60), (450,1439)],
["Exchange", (480,1080)],
["Gingers Express", (480, 960)],
["Heinz Cafe", (510,840)],
["Innovation", (660,870),(1020,1260)],
["iNoodle", (480,980)],
["Nakama", (660, 870), (1020, 1260)],
["Nourish", (630, 1110)],
["Pomegranate", (660, 870)],
["La Prima", (480,960)],
["Realwich", (630, 960)],
["Rohr Cafe", (420,1140)],
["Rooted", (630, 1260)],
["Pure", (420, 1260)],
["Schatz", (450,630),(1020,1260)],
["Seiber Cafe", (450, 900)],
["Stephanie's", (0,1439)],
["Tartan Express", (660, 960)],
["Taste of India", (660, 840), (1020, 1260)],
["Underground", (0, 120), (510, 1439)],
["Zebra Lounge", (480, 1020)]]

restaurantsSaturdays = [
["Au Bon Pain", (0,120), (420,1439)],
["BBG", (0,0)],
["Bibimbap", (0,0)],
["Bowl Life", (0,0)],
["BYOB", (1020, 1260)],
["Resnik Cafe", (0,120), (480,1439)],
["Create", (0,0)],
["Cucina", (1020, 1380)],
["Entropy", (0,60), (600,1439)],
["Exchange", (600,870)],
["El Gallo", (630,1320)],
["Gingers Express", (0,0)],
["Heinz Cafe", (0,0)],
["Innovation", (1020,1260)],
["iNoodle", (660,1200)],
["Nakama", (0,0)],
["Nourish", (0,0)],
["Pomegranate", (0,0)],
["La Prima", (0,0)],
["Realwich", (0,0)],
["Rohr Cafe", (0,0)],
["Pure", (630, 1110)],
["Rooted", (0,0)],
["Schatz", (630,870)],
["Seiber Cafe", (0,0)],
["Stephanie's", (0,1439)],
["Tartan Express", (0,0)],
["Taste of India", (1020,1260)],
["Underground", (0, 120), (510, 1439)],
["Zebra Lounge", (0,0)]]

restaurantsSundays = [
["Au Bon Pain", (0,120), (420,1439)],
["BBG", (0,0)],
["Bibimbap", (0,0)],
["Bowl Life", (0,0)],
["BYOB", (1020, 1260)],
["Resnik Cafe", (0,120), (480,1439)],
["Create", (0,0)],
["Cucina", (1020, 1380)],
["Entropy", (0,180), (600,1439)],
["Exchange", (600,870)],
["El Gallo", (630,1320)],
["Gingers Express", (0,0)],
["Heinz Cafe", (0,0)],
["Innovation", (1020,1260)],
["iNoodle", (660,1200)],
["Nakama", (0,0)],
["Nourish", (0,0)],
["Pomegranate", (0,0)],
["La Prima", (0,0)],
["Realwich", (0,0)],
["Rohr Cafe", (0,0)],
["Pure", (630, 1110)],
["Rooted", (0,0)],
["Schatz", (630,870)],
["Seiber Cafe", (0,0)],
["Stephanie's", (0,1439)],
["Tartan Express", (0,0)],
["Taste of India", (1020,1260)],
["Underground", (0, 120), (510, 1439)],
["Zebra Lounge", (0,0)]]

