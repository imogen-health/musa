from openai import OpenAI
from app.environment import Environment

def handle_message(message):
    chat_message = {
        "role": "user",
        "content": content_format.format(message=message),
    }

    chat_completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[chat_message],
    )

    return chat_completion.choices[0].message.content

client = OpenAI(api_key=Environment.OPENAI_API_KEY)
content_format = \
"""
Considere que o Governo do Estado de Pernambuco oferece os serviços a seguir:

Grupo 0: "ATENDIMENTO AO PÚBLICO"
- "Ouvidoria da Mulher": A Ouvidoria da Mulher é um canal de comunicação entre a população e a Secretaria da Mulher, para o acolhimento de sugestões, solicitações, elogios, reclamações e denúncias, com escuta qualificada dirigida principalmente às mulheres urbanas e rurais de todo o estado. Você pode entrar em contato através de um dos seguintes canais:

* Central de Teleatendimento - Cidadã Pernambucana (0800.281.8187): funciona 24h de domingo a domingo, inclusive feriados. A ligação é gratuita e pode ser realizada através de telefone fixo e/ou celular.
* Atendimento presencial: na sede da SecMulher-PE, (Rua Cais do Apolo, nº222, 4º andar – Prédio Porto Digital, bairro do Recife – Recife/PE),de segunda a sexta-feira, das 8h às 12h e das 13h às 17h.
* Atendimento telefônico: pelo número (81) 3183-2963, em dias úteis, de segunda a sexta-feira, das 8h às 12h e das 13h às 17h.
* E-mail: as demandas podem ser encaminhadas por e-mail, para o endereço eletrônico ouvidoria@secmulher.pe.gov.br
* Formulário eletrônico: As demandas também podem ser registradas através do site da Secretaria da mulher http://www.secmulher.pe.gov.br, no menu ouvidoria.
* Cartas e Oficio: As cartas e/ou oficio devem ser encaminhadas para o seguinte endereço: Rua Cais do Apolo, nº 222, 4º andar – Prédio Porto Digital, bairro do Recife – Recife/PE, CEP: 50030-905


Grupo 1: "SERVIÇOS DE PROTEÇÃO ÀS MULHERES EM SITUAÇÃO DE VIOLÊNCIA DOMÉSTICA E FAMILIAR"
- "Serviço de Proteção, Atendimento e Abrigamento às Mulheres em Situação de
Violência Doméstica e Familiar sob Risco de Morte": é voltado para o atendimento e acolhimento de mulheres que se encontram em situação de violência doméstica e familiar sob risco eminente de morte. Tem caráter continuado e visa proteger a integridade física e psicológica das mulheres, através do abrigamento provisório em endereços sigilosos. Este serviço tem como público alvo mulheres residentes no estado de Pernambuco em situação de violência doméstica e familiar sob risco de morte, e que não disponha de local seguro e protegido para se abrigar. O serviço deve ser solicitado pela instituição que está realizando o atendimento à mulher vítima de violência, depois de identificada o risco de morte e a indisponibilidade de local seguro e protegido para a mulher. O serviço funciona 24 horas por dia, incluindo finais de semana e feriados, podendo ser solicitado a qualquer momento, pelo profissional da instituição,através do telefone de plantão do serviço.
- "190 Mulher": consiste no cadastramento de mulheres em situação de violência, garantindo-lhes condição de prioridade na abordagem emergencial da Policia Militar quando acionado o 190. A mulher deve procurar qualquer serviço da rede de atendimento à mulher em situação de violência relatar o que está se passando e informar do interesse no cadastro.
- "Patrulha Maria da Penha": É um atendimento especializado, com caráter ostensivo e preventivo, realizado pela Policia Militar para ao acompanhamento das mulheres em situação de violência doméstica e familiar que solicitaram Medidas Protetivas de Urgência. A Patrulha Maria da Penha tem como objetivo fiscalizar o cumprimento das Medidas Protetivas de Urgência aplicadas ao agressor. O público-alvo são mulheres em situação de violência doméstica e familiar que solicitam medidas protetivas de urgência nas delegacias especializadas ou comuns e que manifestam o desejo de receber a visita da patrulha. É necessário registrar Boletim de Ocorrência e solicitar Medidas Protetivas de Urgência em qualquer Delegacia Especializada de Atendimento à Mulher ou em Delegacias Comuns.

Grupo 2: "CAMPANHAS EDUCATIVAS PARA PREVENÇÃO DA VIOLÊNCIA CONTRA A MULHER"
- "Campanha Violência Contra a Mulher é Jogo Sujo": A campanha foi pensada para ser divulgada em eventos esportivos das diversas modalidades realizados em Pernambuco, principalmente durante os jogos de futebol, onde há uma maior concentração de pessoas nos estádios. São disponibilizados materiais educativos como: cartazes e faixas nos estádios de futebol, quadra esportivas, entre outros, para que as pessoas que vão assistir aos jogos esportivos possam vê. Essa campanha é desenvolvida com o apoio da Federação Pernambucana de Futebol e de outras instituições que realizam eventos esportivos.
- "Campanha Violência contra a Mulher não dá Frutos": É uma campanha voltada para atender as mulheres do campo, da floresta e das águas, residentes em comunidades, assentamentos e acampamentos rurais do estado de Pernambuco. Tem como foco principal, informar e orientar as mulheres sobre a violência doméstica e familiar. A campanha utiliza unidades móveis (ônibus adaptado) para chegar até as mulheres nas comunidades rurais, indicadas pelos movimentos sociais que compõem a Comissão Permanente de Mulheres Rurais de Pernambuco – CPMR/PE. No local, o diálogo é direto com as mulheres em rodas de conversas realizadas pelas equipes da Secretaria da Mulher de Pernambuco e dos Organismos Municipais de Políticas para as Mulheres. Além das rodas de conversa, a campanha oferece atendimento psicológico, social e/ou orientação jurídica dentro das unidades móveis, que são adaptadas e equipadas para esse tipo de serviço.

Grupo 3: "PROGRAMAS VOLTADOS PARA A QUALIFICAÇÃO PROFISSIONAL DAS MULHERES"
- "Apoio à Qualificação Para o Emprego": voltado para promover a qualificação e a inserção profissional
das mulheres a partir de 18 anos, incluindo nesse contexto, conteúdos da formação sociopolítica, e oportunizar o desenvolvimento de suas habilidades e competências para o mundo do trabalho. Dessa forma, procura-se aprimorar o seu desempenho produtivo e inseri-la, em condições de igualdade, nos diversos segmentos do mercado produtivo de Pernambuco.
- "Chapéu de Palha Mulher": É um programa voltado para apoiar a superação das desigualdades históricas de gênero, gerando oportunidades de participação ativa, contínua e democrática de mulheres rurais e pescadoras artesanais que se encontram em vulnerabilidade social, decorrente das culturas sazonais da zona canavieira e da fruticultura irrigada, assim como convivendo com as condições adversas para a pesca artesanal durante o período de inverno. O programa promove o fortalecimento sociopolítico e o empoderamento das mulheres, em uma articulação permanente com os movimentos sociais rurais e com organizações sociais de mulheres e feministas. Consiste na oferta cursos de formação sociopolítica, com ênfase em gênero, raça, classe, etnia; acesso aos direitos básicos: saúde, educação, habitação; enfrentamento da violência de gênero contra as mulheres; entre outros temas relevantes ao processo de empoderamento; além de cursos de qualificação profissional voltados para a promoção da autonomia produtiva e econômica das mulheres. O Programa oferta, também, atividades lúdico-pedagógicas para as filhas e filhos, até sete anos de idade, das participantes. O público-alvo são mulheres trabalhadoras rurais com mais de 18 anos do corte da cana de açúcar, da fruticultura irrigada e da pesca artesanal. 
- "Centro da Mulher Metropolitana Julia Santiago": é um espaço de formação para o fortalecimento, produção de conhecimento e empoderamento das mulheres da Região Metropolitana do Recife. O espaço oferece cursos profissionalizantes e de formação sociopolítica, através de parceria com outras instituições, além do serviço de orientação e encaminhamento de mulheres vítimas de violência doméstica e familiar ou que apresente demandas relacionadas às áreas jurídica e psicossocial. Para ter acesso aos cursos e serviços oferecidos pelo centro, é preciso comparecer ao local e se informar sobre a programação ou falar com uma das profissionais presentes. Também é possível se informar pelo telefone (81) 3183-2994, o horário de funcionamento é das 08h às 17h de segunda a sexta-feira.

Considere também que uma mulher do Estado de Pernambuco enviou a seguinte mensagem:

"{message}"

Com base nesta mensagem e nos serviços listados anteriormente, como você aconselharia ela a buscar ajuda do governo do estado? Não dê conselhos de serviços fora desta lista fornecida. Apenas nos casos em que a mensagem não tem relação com os serviços ofertados, indique buscar apoio com a ouvidoria da mulher. Caso a mensagem seja relacionada a um dos serviços ofertados, não adicione os dados de contato da ouvidoria na resposta.
"""