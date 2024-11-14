import json
from utils import get_intents
def get_response(user_input):
    intents = get_intents()
    for intent in intents['intents']:
        if user_input in intent['patterns']:
            return intent['responses'][0]
    return "I didn't understand that."

