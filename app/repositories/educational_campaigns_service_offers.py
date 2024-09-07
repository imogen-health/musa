from app.models.service_offer import ServiceOffer
from app.models.service_offer_group import ServiceOfferGroup


def get_educational_campaigns_service_offers():
    return ServiceOfferGroup(
        name="CAMPANHAS EDUCATIVAS PARA PREVENÇÃO DA VIOLÊNCIA CONTRA A MULHER",
        service_offers=[
            ServiceOffer(
                name="Campanha Violência Contra a Mulher é Jogo Sujo",
                description="A campanha foi pensada para ser divulgada em eventos esportivos das diversas modalidades realizados em Pernambuco, principalmente durante os jogos de futebol, onde há uma maior concentração de pessoas nos estádios. São disponibilizados materiais educativos como: cartazes e faixas nos estádios de futebol, quadra esportivas, entre outros, para que as pessoas que vão assistir aos jogos esportivos possam vê. Essa campanha é desenvolvida com o apoio da Federação Pernambucana de Futebol e de outras instituições que realizam eventos esportivos.",
            ),
            ServiceOffer(
                name="Campanha Violência contra a Mulher não dá Frutos",
                description="É uma campanha voltada para atender as mulheres do campo, da floresta e das águas, residentes em comunidades, assentamentos e acampamentos rurais do estado de Pernambuco. Tem como foco principal, informar e orientar as mulheres sobre a violência doméstica e familiar. A campanha utiliza unidades móveis (ônibus adaptado) para chegar até as mulheres nas comunidades rurais, indicadas pelos movimentos sociais que compõem a Comissão Permanente de Mulheres Rurais de Pernambuco – CPMR/PE. No local, o diálogo é direto com as mulheres em rodas de conversas realizadas pelas equipes da Secretaria da Mulher de Pernambuco e dos Organismos Municipais de Políticas para as Mulheres. Além das rodas de conversa, a campanha oferece atendimento psicológico, social e/ou orientação jurídica dentro das unidades móveis, que são adaptadas e equipadas para esse tipo de serviço.",
            ),
        ],
    )
