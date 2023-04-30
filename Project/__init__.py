from flask import Flask, request, abort

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!', 200

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    if request.method == 'POST':
        print(request.json)
        return 'success', 200
    
    elif request.method == 'GET':
        return 'This is method GET!!!', 200
    
    