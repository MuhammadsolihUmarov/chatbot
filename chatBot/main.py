import re
import chatBot.long_responses as long


def message_prob(user_mes, recognised_words, single_response=False, required_words=[]):
    '''
    Calculates the certainty of a user message based on the presence of recognized words and the 
    percentage of these words in the message. If required_words are specified, the function only 
    returns a certainty score if all required words are present in the message. If single_response 
    is True, the function always returns a certainty score regardless of the presence of required 
    words.

    Parameters:
        user_mes (list): The message to be analyzed, split into a list of words.
        recognised_words (list): A list of words that the function recognizes.
        single_response (bool, optional): If True, the function always returns a certainty score.
        required_words (list, optional): A list of words that must be present in the message for 
            the function to return a certainty score.

    Returns:
        int: The certainty of the message as a percentage (0-100) or 0.
    '''
    message_certainty = 0
    has_req_words = True

    # Count how many recognised words are present in the message
    for word in user_mes:
        if word in recognised_words:
            message_certainty += 1

    # Calculate the percent of recognised words in a user message
    percentage = float(message_certainty) / float(len(recognised_words))

    #if one of required words is not in the user message, set the message does not contain required words and break the loop
    for word in required_words:
        if word not in user_mes:
            has_req_words = False
            break

    #if the response has required words or it is a single response, return message certainty
    if has_req_words or single_response:
        return int(percentage*100) 
    #Otherwise return false
    else:
        return 0


def check_all_messages(message):
    '''
    Checks the given inputs and trains the chatBot to respond to simple questions.
    
    Parameters: 
        message (list): The user message divided into words to be analyzed 
    '''
    highest_prob_l = {}

    def response(bot_res, list_of_words, single_res=False, required_words=[]) -> None:
        '''Takes respective bot response and the list of relative words and lists each of the bot response probabilities
        
        Parameters:
            bot_res (string): The  bot response
            list_of_words (list): The expected words to return certain bot response
            single_res (bool): whether or not it is a single response. Default = False
            required_words (list): required list of words in order to return certain response
            '''
        nonlocal highest_prob_l                                 #nonlocal is used for not initializing seperate memory location for local veriable but connecting it to highest_prob_l memory location
        highest_prob_l[bot_res] = message_prob(
            message, list_of_words, single_res, required_words) #takes the probabilities of each response


    #This training data will be replaced with json or database when the chatbot become larger
    response('Hello!', ['hello', 'hi', 'sup', 'hey', 'heyo'], single_res=True)
    
    response('I\'m doing fine, and you?', [
             'how', 'are', 'you', 'doing'], required_words=['how'])
    
    response('Thank you', ['i', 'love', 'code', 'your', 'amazing',
             'response'], required_words=['like', 'response'])
    
    response(long.CODING, ['chatgpt', 'code', 'write']),
    
    response("Thank you!", ['amazing', 'great', 'super', 'wow'])

    best_match = max(highest_prob_l, key=highest_prob_l.get)     #Find the best answer depending on probability. get function is used to get the key of the dictionary element
    print(highest_prob_l)

    #if the message(s) probablities*100 are less than 1, return one of the sentences signaling that the user message is not recognized
    #Otherwise return best match
    return long.unknown() if highest_prob_l[best_match] < 1 else best_match 


def get_response(user_input):
    '''
    Gets user message and splits to tokens(words) if '\s+|[,;?!.-]\s' is encountered in the sentence
    
    Parameters: 
        userinput (string): The user message to be analyzed
    '''
    splitted_mes = re.split(r'\s+|[,;?!.-]\s', user_input.lower())

    response = check_all_messages(splitted_mes)
    return response


# Starting the chat
# You can use this in local command line tests
'''print("Bot: Hi there!")
while True:
    print('Bot: ' + get_response(input('You: ')))'''
    
    
def mainChatBot(req):
    res = get_response(req)
    return res
