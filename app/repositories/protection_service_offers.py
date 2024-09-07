from app.models.service_offer import ServiceOffer
from app.models.service_offer_group import ServiceOfferGroup


def get_protection_service_offers():
    return ServiceOfferGroup(
        name="SERVIÇOS DE PROTEÇÃO ÀS MULHERES EM SITUAÇÃO DE VIOLÊNCIA DOMÉSTICA E FAMILIAR",
        service_offers=[
            ServiceOffer(
                name="Serviço de Proteção, Atendimento e Abrigamento às Mulheres em Situação de Violência Doméstica e Familiar sob Risco de Morte",
                description="É voltado para o atendimento e acolhimento de mulheres que se encontram em situação de violência doméstica e familiar sob risco eminente de morte. Tem caráter continuado e visa proteger a integridade física e psicológica das mulheres, através do abrigamento provisório em endereços sigilosos. Este serviço tem como público alvo mulheres residentes no estado de Pernambuco em situação de violência doméstica e familiar sob risco de morte, e que não disponha de local seguro e protegido para se abrigar. O serviço deve ser solicitado pela instituição que está realizando o atendimento à mulher vítima de violência, depois de identificada o risco de morte e a indisponibilidade de local seguro e protegido para a mulher. O serviço funciona 24 horas por dia, incluindo finais de semana e feriados, podendo ser solicitado a qualquer momento, pelo profissional da instituição,através do telefone de plantão do serviço.",
            ),
            ServiceOffer(
                name="190 Mulher",
                description="Consiste no cadastramento de mulheres em situação de violência, garantindo-lhes condição de prioridade na abordagem emergencial da Policia Militar quando acionado o 190. A mulher deve procurar qualquer serviço da rede de atendimento à mulher em situação de violência relatar o que está se passando e informar do interesse no cadastro.",
            ),
            ServiceOffer(
                name="Patrulha Maria da Penha",
                description="É um atendimento especializado, com caráter ostensivo e preventivo, realizado pela Policia Militar para ao acompanhamento das mulheres em situação de violência doméstica e familiar que solicitaram Medidas Protetivas de Urgência. A Patrulha Maria da Penha tem como objetivo fiscalizar o cumprimento das Medidas Protetivas de Urgência aplicadas ao agressor. O público-alvo são mulheres em situação de violência doméstica e familiar que solicitam medidas protetivas de urgência nas delegacias especializadas ou comuns e que manifestam o desejo de receber a visita da patrulha. É necessário registrar Boletim de Ocorrência e solicitar Medidas Protetivas de Urgência em qualquer Delegacia Especializada de Atendimento à Mulher ou em Delegacias Comuns.",
            ),
        ],
    )
