from flask import Flask, render_template, request, jsonify
import aiml
import os
from duckduckpy import query

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('chat.html')


@app.route('/ask', methods=['GET', 'POST'])
def parse_request():
    message =  str(request.form['message'])
    query_result = query(message)
    print query_result.answer.text
    if len(query_result.results) > 0 :
        print 'found a solution'
        answer = query_result.results[0].text

    else:
        answer = 'check your input'
    
    print answer
    
    return jsonify({ 'answer': answer})

if __name__ == "__main__":
    app.run(debug=False)    
