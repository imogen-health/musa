from openai import OpenAI
from app.environment import Environment
from app.repositories.service_offers import ServiceOffersRepository


class PromptService(object):

    def __init__(self):
        self.__client = OpenAI(api_key=Environment.OPENAI_API_KEY)
        self.__repository = ServiceOffersRepository()
        self.__content_format = """
Considere que o Governo do Estado de Pernambuco oferece os serviços a seguir:

{services}

Considere também que uma mulher do Estado de Pernambuco enviou a seguinte mensagem:

"{message}"

Com base nesta mensagem e nos serviços listados anteriormente, responda diretamente como ela pode obter ajuda com os serviços ofertados. Não dê conselhos de serviços fora desta lista fornecida. Apenas nos casos em que a mensagem não tem relação com os serviços ofertados, indique buscar apoio com a ouvidoria da mulher. Caso a mensagem seja relacionada a um dos serviços ofertados, não adicione os dados de contato da ouvidoria na resposta. Caso ela queira saber quais são os serviços ofertados, informe a lista de serviços de maneira sucinta.
"""

    def handle_message(self, message):
        chat_message = {
            "role": "user",
            "content": self.__get_prompt_message(message),
        }

        chat_completion = self.__client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[chat_message],
        )

        return chat_completion.choices[0].message.content

    def __get_prompt_message(self, message):
        service_lines = []
        service_offers = self.__repository.get_service_offers()

        for group_index, group in enumerate(service_offers):
            service_lines.append(f'Grupo {group_index + 1}: "{group.name}"')

            for offer in group.service_offers:
                service_lines.append(f'- "{offer.name}": {offer.description}')
            service_lines.append("")

        service_catalog = "\n".join(service_lines)
        return self.__content_format.format(message=message, services=service_catalog)
