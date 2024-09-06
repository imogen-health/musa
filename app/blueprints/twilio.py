from flask import Blueprint, request
from twilio.twiml.messaging_response import MessagingResponse

twilio = Blueprint('twilio', __name__)

@twilio.route('/message', methods=['POST'])
def on_message_received():
    incoming_message = request.values.get('Body', '').lower()
    
    response = MessagingResponse()
    response_message = response.message()
    response_message.body('Hello! You said: {}'.format(incoming_message))

    return str(response)
