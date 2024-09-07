from flask import Blueprint, request
from twilio.twiml.messaging_response import MessagingResponse

from app.services.engine import handle_message
from app.services.logging import get_logger

twilio = Blueprint('twilio', __name__)
logger = get_logger(__name__)

@twilio.route('/message', methods=['POST'])
def on_message_received():
    response = MessagingResponse()

    message_content = request.values.get('Body', '').lower()
    message_type = request.values.get('MessageType', '')
    phone_number = request.values.get('From', '')

    logger.info(f"Received {message_type} message from {phone_number}")

    try:
        response_content = handle_message(message_content)
        response_message = response.message()
        response_message.body(response_content)

        logger.info(f"Sending response back to {phone_number}")
    except Exception as exception:
        logger.error(f"Error while processing message: {exception}")
        response_message.body("Desculpe, não consegui entender sua mensagem. Por favor, tente novamente.")

    return str(response)
