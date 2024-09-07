from flask import Blueprint, request
from twilio.twiml.messaging_response import MessagingResponse

from app.services.prompt import PromptService
from app.instrumentation.logging import Logging

twilio = Blueprint("twilio", __name__)
logger = Logging.get_logger(__name__)
prompt_service = PromptService()


@twilio.route("/message", methods=["POST"])
def on_message_received():
    response = MessagingResponse()

    message_content = request.values.get("Body", "").lower()
    message_type = request.values.get("MessageType", "")
    phone_number = request.values.get("From", "")

    logger.info(f"Received {message_type} message from {phone_number}")

    try:
        response_content = prompt_service.handle_message(message_content)
        response_message = response.message()
        response_message.body(response_content)

        logger.info(f"Sending response back to {phone_number} with {response_content}")
    except Exception as exception:
        message = "Desculpe, não consegui entender sua mensagem."

        logger.error(f"Error while processing message: {exception}")
        response_message.body(message)

    return str(response)
