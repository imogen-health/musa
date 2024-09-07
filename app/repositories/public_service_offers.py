from app.models.service_offer import ServiceOffer
from app.models.service_offer_group import ServiceOfferGroup


def get_public_service_offers():
    return ServiceOfferGroup(
        name="ATENDIMENTO AO PÚBLICO",
        service_offers=[
            ServiceOffer(
                name="Ouvidoria da Mulher",
                description="""
A Ouvidoria da Mulher é um canal de comunicação entre a população e a Secretaria da Mulher, para o acolhimento de sugestões, solicitações, elogios, reclamações e denúncias, com escuta qualificada dirigida principalmente às mulheres urbanas e rurais de todo o estado. Você pode entrar em contato através de um dos seguintes canais:

* Central de Teleatendimento - Cidadã Pernambucana (0800.281.8187): funciona 24h de domingo a domingo, inclusive feriados. A ligação é gratuita e pode ser realizada através de telefone fixo e/ou celular.
* Atendimento presencial: na sede da SecMulher-PE, (Rua Cais do Apolo, nº222, 4º andar – Prédio Porto Digital, bairro do Recife – Recife/PE),de segunda a sexta-feira, das 8h às 12h e das 13h às 17h.
* Atendimento telefônico: pelo número (81) 3183-2963, em dias úteis, de segunda a sexta-feira, das 8h às 12h e das 13h às 17h.
* E-mail: as demandas podem ser encaminhadas por e-mail, para o endereço eletrônico ouvidoria@secmulher.pe.gov.br
* Formulário eletrônico: As demandas também podem ser registradas através do site da Secretaria da mulher http://www.secmulher.pe.gov.br, no menu ouvidoria.
* Cartas e Oficio: As cartas e/ou oficio devem ser encaminhadas para o seguinte endereço: Rua Cais do Apolo, nº 222, 4º andar – Prédio Porto Digital, bairro do Recife – Recife/PE, CEP: 50030-905
            """,
            )
        ],
    )
