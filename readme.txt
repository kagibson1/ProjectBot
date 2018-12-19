ProjectBot by Kellen Gibson (video demonstration: https://www.youtube.com/watch?v=W11rZMJmuLs)


My ProjectBot is a chatbot that will take in input from the user and figure out and return an appropriate response. It constructs a response and then keeps track of the input and output pairs with a dictionary and has a variable that keeps track of the last input. Some of the ways that it constructs responses includes by using the minimum number of edits to handle restaurant name misspellings, keywords to decide if you want to know what restaurants are open, what time a restaurant opens, what time a restaurant closes, and if a restaurant is open. It goes through CMU courses (as JSON) to get specific information about the course (name, description, units, prereqs, coreqs, etc) based on keywords and if you don’t ask a question – constructs a response with NLP that can be edited to be more grammatically correct by the user. It can be trained to give a specific response to an input set by the user. Furthermore, it looks up questions on Wolfram Alpha, dad jokes, weather, and cat jokes using various APIs. It can also detect greetings, terminations, profanity, and answer some basic questions about itself. 

Installation: 
Requires Python 3 
Run the following commands in the command prompt:
	pip install requests
	pip install datetime 
	pip install json
Install GroupMe on your mobile device. 

How to run the project: 

- Download each of the files (functions.py, nlpWork.py, food.py, ProjectBot.py, cmu_course_data.json)
- If you have my phone, run ProjectBot.py and you're set!
- If you want to add ProjectBot to your own group chat, follow instructions on this website to create your own bot (https://dev.groupme.com/tutorials/bots). I used method 1. Choose the group that you would like the bot to live in. Create the bot, note the Bot ID and Group ID. In the ProjectBot.py file, where it says accessToken, replace my access token with yours provided and same with the groupID. Now you're ready to run the bot! Just run ProjectBot.py!
