from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route('/message', methods=['POST'])
def on_message_received():
    incoming_message = request.values.get('Body', '').lower()
    
    response = MessagingResponse()
    response_message = response.message()

    response_message.body('Hello! You said: {}'.format(incoming_message))

    return str(response)


if __name__ == '__main__':
    app.run()