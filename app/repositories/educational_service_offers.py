from app.models.service_offer import ServiceOffer
from app.models.service_offer_group import ServiceOfferGroup


def get_educational_service_offers():
    return ServiceOfferGroup(
        name="PROGRAMAS VOLTADOS PARA A QUALIFICAÇÃO PROFISSIONAL DAS MULHERES",
        service_offers=[
            ServiceOffer(
                name="Apoio à Qualificação Para o Emprego",
                description="voltado para promover a qualificação e a inserção profissional das mulheres a partir de 18 anos, incluindo nesse contexto, conteúdos da formação sociopolítica, e oportunizar o desenvolvimento de suas habilidades e competências para o mundo do trabalho. Dessa forma, procura-se aprimorar o seu desempenho produtivo e inseri-la, em condições de igualdade, nos diversos segmentos do mercado produtivo de Pernambuco.",
            ),
            ServiceOffer(
                name="Chapéu de Palha Mulher",
                description="É um programa voltado para apoiar a superação das desigualdades históricas de gênero, gerando oportunidades de participação ativa, contínua e democrática de mulheres rurais e pescadoras artesanais que se encontram em vulnerabilidade social, decorrente das culturas sazonais da zona canavieira e da fruticultura irrigada, assim como convivendo com as condições adversas para a pesca artesanal durante o período de inverno. O programa promove o fortalecimento sociopolítico e o empoderamento das mulheres, em uma articulação permanente com os movimentos sociais rurais e com organizações sociais de mulheres e feministas. Consiste na oferta cursos de formação sociopolítica, com ênfase em gênero, raça, classe, etnia; acesso aos direitos básicos: saúde, educação, habitação; enfrentamento da violência de gênero contra as mulheres; entre outros temas relevantes ao processo de empoderamento; além de cursos de qualificação profissional voltados para a promoção da autonomia produtiva e econômica das mulheres. O Programa oferta, também, atividades lúdico-pedagógicas para as filhas e filhos, até sete anos de idade, das participantes. O público-alvo são mulheres trabalhadoras rurais com mais de 18 anos do corte da cana de açúcar, da fruticultura irrigada e da pesca artesanal.",
            ),
            ServiceOffer(
                name="Centro da Mulher Metropolitana Julia Santiago",
                description="é um espaço de formação para o fortalecimento, produção de conhecimento e empoderamento das mulheres da Região Metropolitana do Recife. O espaço oferece cursos profissionalizantes e de formação sociopolítica, através de parceria com outras instituições, além do serviço de orientação e encaminhamento de mulheres vítimas de violência doméstica e familiar ou que apresente demandas relacionadas às áreas jurídica e psicossocial. Para ter acesso aos cursos e serviços oferecidos pelo centro, é preciso comparecer ao local e se informar sobre a programação ou falar com uma das profissionais presentes. Também é possível se informar pelo telefone (81) 3183-2994, o horário de funcionamento é das 08h às 17h de segunda a sexta-feira.",
            ),
        ],
    )
