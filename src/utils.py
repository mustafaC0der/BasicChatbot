import json

def get_intents():
    with open('data/intents.json') as file:
        intents = json.load(file)
    return intents
