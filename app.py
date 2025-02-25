from flask import Flask, request, jsonify
from chat import chatbot

app=Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/ask", methods=["POST"])
def ask():
    message=str(request.form['messageText'])
    bot_response=chatbot(message)
    return jsonify({"status":"OK","response":bot_response})

if __name__=="__main__":
    app.run()
    