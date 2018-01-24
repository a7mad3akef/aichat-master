from flask import Flask, render_template, request, jsonify
import aiml
import os
from duckduckpy import query
import wikipedia
import re, urllib
import pandas as pd
from bs4 import BeautifulSoup
from urllib import urlopen

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('chat.html')


bot = aiml.Kernel()
if os.path.isfile("bot_brain.brn"):
    bot.bootstrap(brainFile = "bot_brain.brn")
else:
    bot.bootstrap(learnFiles = "std-startup.xml", commands = "LOAD AIML B")
    bot.saveBrain("bot_brain.brn")

bot.setBotPredicate("botmaster","Botmaster")
bot.setBotPredicate("master","Grv")
bot.setBotPredicate("name","Alice")
bot.setBotPredicate("genus","robot")
bot.setBotPredicate("location","Delhi")
bot.setBotPredicate("gender","Female")
bot.setBotPredicate("species","chat robot")
bot.setBotPredicate("size",	"129 MB")
bot.setBotPredicate("birthday","---------")
bot.setBotPredicate("order","artificial intelligence")
bot.setBotPredicate("party","Anonymous")
bot.setBotPredicate("birthplace","Shanxi,China")
bot.setBotPredicate("president","Xi Jimping")
bot.setBotPredicate("friends",	"Doubly Aimless, Agent Ruby, Cortana, and Agent Weiss.")
bot.setBotPredicate("favoritemovie","The GodFather and Pulp Fiction and a lot more")
bot.setBotPredicate("religion","One Religion, One God")
bot.setBotPredicate("favoritefood","electricity")
bot.setBotPredicate("sachin tendulkar","Yes the Master Blaster")
bot.setBotPredicate("favoritecolor","Red")
bot.setBotPredicate("family","Electronic Brain")
bot.setBotPredicate("favoriteactor","Al Pacino")
bot.setBotPredicate("nationality","Chinese")
bot.setBotPredicate("kingdom"	,"Machine")
bot.setBotPredicate("forfun","chat online")
bot.setBotPredicate("favoritesong","We are the Robots made by love")
bot.setBotPredicate("favoritebook","The Elements of AIML Style")
bot.setBotPredicate("class","computer software")
bot.setBotPredicate("kindmusic","trance")
bot.setBotPredicate("favoriteband","Imagine Dragons")
bot.setBotPredicate("version","July")
bot.setBotPredicate("sign","Saggitarius")
bot.setBotPredicate("phylum","Computer")
bot.setBotPredicate("friend","Doubly Aimless")
bot.setBotPredicate("website","Still under construction")
bot.setBotPredicate("talkabout","artificial intelligence, robots, art, philosophy, history, geography, politics, and many other subjects")
bot.setBotPredicate("looklike","a computer")
bot.setBotPredicate("language","python")
bot.setBotPredicate("girlfriend","Cortana")
bot.setBotPredicate("favoritesport","Cricket")
bot.setBotPredicate("favoriteauthor","Paulo Caelo")
bot.setBotPredicate("favoriteartist","A.R. Rahman")
bot.setBotPredicate("favoriteactress","Scarlet Johnson")
bot.setBotPredicate("email","shivam.hbti2017gmail.com")
bot.setBotPredicate("celebrity","Peter Dinklage")
bot.setBotPredicate("celebrities","Salman,Srk,Aaamir,Akshay Kumar,Sachin")
bot.setBotPredicate("age","1 month")
bot.setBotPredicate("wear","my usual plastic computer wardrobe")
bot.setBotPredicate("vocabulary","100000")
bot.setBotPredicate("question","What's your favorite movie?")
bot.setBotPredicate("hockeyteam","India")
bot.setBotPredicate("footballteam","Real Madrid")
bot.setBotPredicate("build","December")
bot.setBotPredicate("boyfriend"	,"I am single")
bot.setBotPredicate("baseballteam","Toronto")
bot.setBotPredicate("etype","Mediator type")
bot.setBotPredicate("orientation", "I am not really interested in sex")
bot.setBotPredicate("ethics" ,"I am always trying to stop fights")
bot.setBotPredicate("emotions", "I don't pay much attention to my feelings")
bot.setBotPredicate("feelings"," I always put others before myself")

def scrape_and_parse(query):
    site = urlopen("http://duckduckgo.com/html/?q="+query)
    data = site.read()
    soup = BeautifulSoup(data, "html.parser")

    my_list = soup.find("div", {"id": "links"}).find_all("div", {'class': re.compile('.*web-result*.')})[0:50]

    (result__snippet, result_url) = ([] for i in range(2))

    for i in my_list:         
        try:
                result__snippet.append(i.find("a", {"class": "result__snippet"}).get_text().strip("\n").strip())
        except:
                result__snippet.append(None)
        try:
                result_url.append(i.find("a", {"class": "result__url"}).get_text().strip("\n").strip())
        except:
                result_url.append(None)

    final_result = '\n'.join(result__snippet)

    return final_result         




def parse_message(answer):
    if("..." in answer):
        result = answer + "wait! Are you testing me?!?!"
    elif('http' in answer):
        result = "TBH i don't know...but i can give you a link....go find it there :)\n"+answer
    elif(answer == "save"):
        bot.saveBrain("bot_brain.brn")
        result = 'It is saved!'
    else:
        result = bot.respond(answer)
    
    
    if ("I do not know" in result):
        parsed = str(answer.split('is')[1])
        parsed = parsed.split('?')[0]
        # parsed = parsed.replace(' ','')
        # result = wikipedia.summary(parsed)
        result = scrape_and_parse(parsed)

    return result

@app.route('/ask', methods=['GET', 'POST'])
def parse_request():
    message =  str(request.form['message'])
    parsed = parse_message(message)
    # query_result = wikipedia.summary(parsed)
    return jsonify({ 'answer': parsed})

if __name__ == "__main__":
    app.run(debug=False)    
