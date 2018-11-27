import datetime 
from datetime import date


def findDate():
    return datetime.datetime.today().strftime('%A')

def currTimeMinutes():
    return int(datetime.datetime.today().strftime('%H'))*60 + int(datetime.datetime.today().strftime('%M'))
    
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

restaurantsWeekdays = [
["Au Bon Pain", (0,120), (420,1439)],
["Black Bar Grill", (630, 1260)],
["Bibimbap",(630,1260)],
["Bowl Life", (630, 1260)],
["BYOB", (660, 870), (1020, 1260)],
["Carnegie Mellon Cafe", (0,120), (420,1439)],
["Create", (630, 1260)],
["Cucina", (660, 1380)],
["El Gallo de Oro", (630,1320)],
["Entropy", (0,180), (450,1439)],
["The Exchange", (480,1200)],
["Gingers Express", (480, 960)],
["Heinz Cafe", (510,1080)],
["Innovation Kitchen", (660,870),(1020,1260)],
["iNoodle", (480,1200)],
["Rothberg's Roasters Maggie Murph", (0,1439)],
["Nakama", (660, 870), (1020, 1260)],
["Nourish", (630, 1110)],
["Pomegranate", (660, 1260)],
["La Prima", (480,1080)],
["Realwich", (630, 960)],
["Rohr Cafe", (420,1140)],
["Pure", (420, 1260)],
["Rooted", (630, 1260)],
["Rothberg's Roasters Ruge", (480, 1200)],
["Schatz", (450,630),(1020,1260)],
["Seiber Cafe", (450, 900)],
["Stephanie's Market C", (0,1439)],
["Tartan Express", (660, 1170)],
["Taste of India", (660, 840), (1020, 1260)],
["The Underground", (0, 120), (510, 1439)],
["Zebra Lounge", (480, 1020)]]

restaurantsFridays = [
["Au Bon Pain", (0,120), (420,1439)],
["Black Bar Grill", (630, 1260)],
["Bibimbap", (630,1260)],
["Bowl Life", (630, 1260)],
["BYOB", (660, 870), (1020, 1260)],
["Carnegie Mellon Cafe", (0,120), (420,1439)],
["Create", (630, 1260)],
["Cucina", (660, 1380)],
["El Gallo de Oro", (630,1320)],
["Entropy", (0,60), (450,1439)],
["The Exchange", (480,1080)],
["Gingers Express", (480, 960)],
["Heinz Cafe", (510,840)],
["Innovation Kitchen", (660,870),(1020,1260)],
["iNoodle", (480,980)],
["Rothberg's Roasters Maggie Murph", (0,1439)],
["Nakama", (660, 870), (1020, 1260)],
["Nourish", (630, 1110)],
["Pomegranate", (660, 870)],
["La Prima", (480,960)],
["Realwich", (630, 960)],
["Rohr Cafe", (420,1140)],
["Rooted", (630, 1260)],
["Rothberg's Roasters Ruge", (480, 1200)],
["Pure", (420, 1260)],
["Schatz", (450,630),(1020,1260)],
["Seiber Cafe", (450, 900)],
["Stephanie's Market C", (0,1439)],
["Tartan Express", (660, 960)],
["Taste of India", (660, 840), (1020, 1260)],
["The Underground", (0, 120), (510, 1439)],
["Zebra Lounge", (480, 1020)]]

restaurantsSaturdays = [
["Au Bon Pain", (0,120), (420,1439)],
["Black Bar Grill", (0,0)],
["Bibimbap", (0,0)],
["Bowl Life", (0,0)],
["BYOB", (1020, 1260)],
["Carnegie Mellon Cafe", (0,120), (480,1439)],
["Create", (0,0)],
["Cucina", (1020, 1380)],
["Entropy", (0,60), (600,1439)],
["The Exchange", (600,870)],
["El Gallo de Oro", (630,1320)],
["Gingers Express", (0,0)],
["Heinz Cafe", (0,0)],
["Innovation Kitchen", (1020,1260)],
["iNoodle", (660,1200)],
["Rothberg's Roasters Maggie Murph", (540,1020)],
["Nakama", (0,0)],
["Nourish", (0,0)],
["Pomegranate", (0,0)],
["La Prima", (0,0)],
["Realwich", (0,0)],
["Rohr Cafe", (0,0)],
["Pure", (630, 1110)],
["Rooted", (0,0)],
["Rothberg's Roasters Ruge", (0,0)],
["Schatz", (630,870)],
["Seiber Cafe", (0,0)],
["Stephanie's Market C", (0,1439)],
["Tartan Express", (0,0)],
["Taste of India", (1020,1260)],
["The Underground", (0, 120), (510, 1439)],
["Zebra Lounge", (0,0)]]

restaurantsSundays = [
["Au Bon Pain", (0,120), (420,1439)],
["Black Bar Grill", (0,0)],
["Bibimbap", (0,0)],
["Bowl Life", (0,0)],
["BYOB", (1020, 1260)],
["Carnegie Mellon Cafe", (0,120), (480,1439)],
["Create", (0,0)],
["Cucina", (1020, 1380)],
["Entropy", (0,180), (600,1439)],
["The Exchange", (600,870)],
["El Gallo de Oro", (630,1320)],
["Gingers Express", (0,0)],
["Heinz Cafe", (0,0)],
["Innovation Kitchen", (1020,1260)],
["iNoodle", (660,1200)],
["Rothberg's Roasters Maggie Murph", (720,1439)],
["Nakama", (0,0)],
["Nourish", (0,0)],
["Pomegranate", (0,0)],
["La Prima", (0,0)],
["Realwich", (0,0)],
["Rohr Cafe", (0,0)],
["Pure", (630, 1110)],
["Rooted", (0,0)],
["Rothberg's Roasters Ruge", (0,0)],
["Schatz", (630,870)],
["Seiber Cafe", (0,0)],
["Stephanie's Market C", (0,1439)],
["Tartan Express", (0,0)],
["Taste of India", (1020,1260)],
["The Underground", (0, 120), (510, 1439)],
["Zebra Lounge", (0,0)]]

