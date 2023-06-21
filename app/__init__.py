from flask import Flask, request, jsonify, render_template
from flask_restful import Api
import openai
import os

genaibox = Flask(__name__,static_url_path='/static')

api = Api(genaibox, prefix='/api')

### OBJECTS AND FUNCTIONS
class ChatGPT3(object):
    def __init__(self, model, temp, max_tokens, top_p, frequency_penalty, presence_penalty, context=''):
        openai_api_key = os.environ.get('API_KEY')
        # (7) chosen parameters for example
        self.model = model
        self.context = context
        self.temp = temp                           # Values: 0.0 - 1.0
        self.max_tokens = max_tokens               # Values: 0 - 4096
        self.top_p = top_p                         # Values: 0.0 - 1.0
        self.frequency_penalty = frequency_penalty # Values: 0.0 - 1.0
        self.presence_penalty = presence_penalty   # Values: 0.0 - 1.0

    def get_response(self, text):
        openai.api_key = self.openai_api_key
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=[{'role':'user','content':text}],
            temperature=self.temp,
            max_tokens=self.max_tokens,
            top_p=self.top_p,
            frequency_penalty=self.frequency_penalty,
            presence_penalty=self.presence_penalty
        )
        return response.choices[0].message['content'].strip()

    def chat(self, text):
        # Tell the model what the Context/History is so that it won't respond to past questions
        response = self.get_response("Context:" + self.context + "Prompt:" + text)

        # Add to the conversation history
        self.context += text + "\n"

        #print('\n\nContext:\n{}'.format(self.context))
        return response
    
        '''
        response = self.get_response(text)
        logging.info(response)
        return response
        '''


### Parameter Tunning
# Summarizer Box(1):
    # Low Temperature
    # Large Frequency Penalty (Avoid Redundant Summaries)
# NYC Guide Box(2):
    # Medium Temperature (More relaxed, Unpredicable)
    # Higher Top-P (Wordiness)
    # No Frequency Penalty (Redundancy Acceptable)
# Computer Engineering Principles Box(3):
    # Low Temperature (Predictable)
    # Small Frequency Penalty (Small Repetition Acceptable)
# gpt-3.5-turbo-16k
    # 16,384 tokens
    # Same capabilities as the standard gpt-3.5-turbo model but with 4 times the context.
# MODEL, TEMP, MAX_TOKENS, TOP-P, FREQ_PEN, PRES_PEN
Box1 = ChatGPT3('gpt-3.5-turbo-16k', 0.1, 500, 0.1, 0.5, 0.0)
Box2 = ChatGPT3('gpt-3.5-turbo-16k', 0.5, 500, 0.3, 0.0, 0.0)
Box3 = ChatGPT3('gpt-3.5-turbo-16k', 0.1, 300, 0.2, 0.2, 0.0)


### ENDPOINTS

@genaibox.route("/")
def index():
    return render_template("index.html")

# '''
@genaibox.route('/process', methods=['POST'])
def process():
    prompt = request.form['user_input']
    generated_text = prompt


    return render_template('index.html', data=generated_text)  # Render template for regular form submission
# '''

'''
@genaibox.route('/process', methods=['POST'])
def process():
    prompt = request.form['user_input']
    

    #generated_text = Box1.chat(prompt)
    generated_text = prompt

    #return render_template('index.html', data=generated_text)
    return render_template('index.html', data=generated_text)
'''