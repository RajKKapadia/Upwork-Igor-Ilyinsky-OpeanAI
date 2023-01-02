from helper.openai_api import text_complition
from flask import Flask, request, jsonify
from dotenv import load_dotenv
load_dotenv()


app = Flask(__name__)


@app.route('/')
def home():
    return 'All is well...'


@app.route('/openai_api/', methods=['POST'])
def openai_api():

    if request.is_json:
        data = request.get_json()
        result = text_complition(data['query'])
        if result['status'] == 1:
            return result
        else:
            return jsonify(
                {
                    'response': 'Error at OpenAI.',
                    'status': 0
                }
            )
    else:
        return jsonify(
            {
                'response': 'Bad request, provide the body with query key.',
                'status': -1
            }
        )
