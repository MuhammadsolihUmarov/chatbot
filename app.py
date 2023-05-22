from flask import Flask, render_template, request, json, jsonify
from chatBot.main import mainChatBot

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST']) #Responds to only GET and POST methods
def index():
    if request.method == 'POST':
        name = json.loads(request.data).get('message') #Gets load from API body
        
        if name is None:
            print("Could not find message keyword") #this is for debugging purposes
            raise KeyError
        
        response = mainChatBot(name)  # Calls the console app's logic to generate the response
        response = {'message': response}
        return jsonify(response)
    
    # For GET requests, simply renders the form.html template without any specific data
    return render_template('form.html')


if __name__ == '__main__':
    app.run(debug=True)
