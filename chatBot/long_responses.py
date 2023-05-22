import random

CODING = "I cannot write code like ChatGPT yet"
DONOTKNOW = "I cannot respond your request, sorry"

def unknown():
    '''Gets no parameter but returns sentance specifying that the message is not understood'''
    response = ['Could you please rephrase that?',
                "...",
                "Sounds about right",
                "I cannot respond your request, sorry",
                "What does it mean?"][random.randrange(4)]
    return response