from flask import Blueprint, request
from twilio.twiml.messaging_response import MessagingResponse

from app.services.engine import handle_message

twilio = Blueprint('twilio', __name__)

@twilio.route('/message', methods=['POST'])
def on_message_received():
    incoming_message = request.values.get('Body', '').lower()
    response_content = handle_message(incoming_message)
    
    response = MessagingResponse()
    response_message = response.message()
    response_message.body(response_content)

    return str(response)
