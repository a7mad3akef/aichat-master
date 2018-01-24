# # from duckduckpy import query

# # r = query('1+1')
# # print r.type

# # print query('Python').type

# import wikipedia
# # print wikipedia.summary("bitcoin")
# # result = wikipedia.page("bitcoin")
# # print result.content
# import aiml, os


# bot = aiml.Kernel()
# if os.path.isfile("bot_brain.brn"):
#     bot.bootstrap(brainFile = "bot_brain.brn")
# else:
#     bot.bootstrap(learnFiles = "std-startup.xml", commands = "LOAD AIML B")
#     bot.saveBrain("bot_brain.brn")


# bot.setBotPredicate("botmaster","Botmaster")
# bot.setBotPredicate("master","Grv")
# bot.setBotPredicate("name","Alice")
# bot.setBotPredicate("genus","robot")
# bot.setBotPredicate("location","Delhi")
# bot.setBotPredicate("gender","Female")
# bot.setBotPredicate("species","chat robot")
# bot.setBotPredicate("size",	"129 MB")
# bot.setBotPredicate("birthday","---------")
# bot.setBotPredicate("order","artificial intelligence")
# bot.setBotPredicate("party","Anonymous")
# bot.setBotPredicate("birthplace","Shanxi,China")
# bot.setBotPredicate("president","Xi Jimping")
# bot.setBotPredicate("friends",	"Doubly Aimless, Agent Ruby, Cortana, and Agent Weiss.")
# bot.setBotPredicate("favoritemovie","The GodFather and Pulp Fiction and a lot more")
# bot.setBotPredicate("religion","One Religion, One God")
# bot.setBotPredicate("favoritefood","electricity")
# bot.setBotPredicate("sachin tendulkar","Yes the Master Blaster")
# bot.setBotPredicate("favoritecolor","Red")
# bot.setBotPredicate("family","Electronic Brain")
# bot.setBotPredicate("favoriteactor","Al Pacino")
# bot.setBotPredicate("nationality","Chinese")
# bot.setBotPredicate("kingdom"	,"Machine")
# bot.setBotPredicate("forfun","chat online")
# bot.setBotPredicate("favoritesong","We are the Robots made by love")
# bot.setBotPredicate("favoritebook","The Elements of AIML Style")
# bot.setBotPredicate("class","computer software")
# bot.setBotPredicate("kindmusic","trance")
# bot.setBotPredicate("favoriteband","Imagine Dragons")
# bot.setBotPredicate("version","July")
# bot.setBotPredicate("sign","Saggitarius")
# bot.setBotPredicate("phylum","Computer")
# bot.setBotPredicate("friend","Doubly Aimless")
# bot.setBotPredicate("website","Still under construction")
# bot.setBotPredicate("talkabout","artificial intelligence, robots, art, philosophy, history, geography, politics, and many other subjects")
# bot.setBotPredicate("looklike","a computer")
# bot.setBotPredicate("language","python")
# bot.setBotPredicate("girlfriend","Cortana")
# bot.setBotPredicate("favoritesport","Cricket")
# bot.setBotPredicate("favoriteauthor","Paulo Caelo")
# bot.setBotPredicate("favoriteartist","A.R. Rahman")
# bot.setBotPredicate("favoriteactress","Scarlet Johnson")
# bot.setBotPredicate("email","shivam.hbti2017gmail.com")
# bot.setBotPredicate("celebrity","Peter Dinklage")
# bot.setBotPredicate("celebrities","Salman,Srk,Aaamir,Akshay Kumar,Sachin")
# bot.setBotPredicate("age","1 month")
# bot.setBotPredicate("wear","my usual plastic computer wardrobe")
# bot.setBotPredicate("vocabulary","100000")
# bot.setBotPredicate("question","What's your favorite movie?")
# bot.setBotPredicate("hockeyteam","India")
# bot.setBotPredicate("footballteam","Real Madrid")
# bot.setBotPredicate("build","December")
# bot.setBotPredicate("boyfriend"	,"I am single")
# bot.setBotPredicate("baseballteam","Toronto")
# bot.setBotPredicate("etype","Mediator type")
# bot.setBotPredicate("orientation", "I am not really interested in sex")
# bot.setBotPredicate("ethics" ,"I am always trying to stop fights")
# bot.setBotPredicate("emotions", "I don't pay much attention to my feelings")
# bot.setBotPredicate("feelings"," I always put others before myself")

# while True:
#     print bot.respond(raw_input("Enter your message >> "))    
# message = 'what is bitcoin?'
# parsed = str(message.split('is')[1])
# parsed = parsed.split('?')[0]
# parsed = parsed.replace(' ','')
# print wikipedia.summary(parsed)

# from duckduckpy import query

# r = query("example")
# for i in r.related_searches:
#     if i.text:
#         print i.text

# import re, urllib
# import pandas as pd
# from bs4 import BeautifulSoup
# from urllib import urlopen

# import bs4 as bs
# from urllib import request


# # declare some needed variables
# link = 'http://www.heart.co.uk/radio/last-played-songs/'
# sauce = request.urlopen(link).read()
# soup = bs.BeautifulSoup(sauce, 'lxml')

# query = "Edinburg"
# site = urlopen("http://duckduckgo.com/html/?q="+query)
# data = site.read()
# soup = BeautifulSoup(data, "html.parser")

# # print(soup)
# my_list = soup.find("div", {"id": "links"}).find_all("div", {'class': re.compile('.*web-result*.')})[0:15]


# (result__snippet, result_url) = ([] for i in range(2))

# for i in my_list:         
#       try:
#             result__snippet.append(i.find("a", {"class": "result__snippet"}).get_text().strip("\n").strip())
#       except:
#             result__snippet.append(None)
#       try:
#             result_url.append(i.find("a", {"class": "result__url"}).get_text().strip("\n").strip())
#       except:
#             result_url.append(None)

# # print result__snippet
# final_result = '-'.join(result__snippet)

# print final_result
