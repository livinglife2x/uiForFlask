#!/usr/bin/env python
from flask import Flask, render_template,Response,make_response
import os
from ibm_watson import AssistantV2
import random
from random import randint
import json
#import report
from io import StringIO
from waitress import serve
app = Flask(__name__)
conversation = AssistantV2(
    iam_apikey = 'U4z0zd0HF27cfJFmIAxilZMR9f92muwBEVb8FPwTdXWC',
    url='https://gateway.watsonplatform.net/assistant/api',
    version='2019-05-19')
session = conversation.create_session("4bb02d7f-606b-4d47-848f-8296fd7928a2").get_result()
variables  = None
#context_val = {}

@app.route('/')
@app.route('/index')
def chat():
    return render_template('chat.html')

@app.route('/send_message/<message>')
def send_mesage(message):
    text = ''
    response = conversation.message(
        assistant_id = '4bb02d7f-606b-4d47-848f-8296fd7928a2',
        session_id= session['session_id'],input={'text': str(message)
            }
        ).get_result()
    variables =  response['output'].get('user_defined')
    #context = response['context']['skills']['main skill']['user_defined']
    
    for i in response['output']['generic']:
        text = text+ i['text']+'\n'
        return text
if __name__ == '__main__':
    port = int(os.getenv('PORT', 8082))
    debug_var = False
    app.run(host='0.0.0.0', port=port, debug=debug_var)
