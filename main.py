import streamlit as ql_hk12
import folium as a1k7_89
from streamlit_folium import folium_static
from base import add_vac, add_horario, retrieve_vac, retrieve_horario, filtroHoras, filtroVac
from time import sleep, gmtime, strftime


ql_hk12.set_page_config(
    page_title="Estoque de Vacina Rio de Janeiro",
    page_icon="imag_ens/healthcare.ico",
    layout="wide",
    initial_sidebar_state="expanded"
)

dictAuth = {'Nenhum' : 'Selecionado', 'Planetario': ['OneDrive', 'Planetário_da_Gávea'],
            'Tijuca Tenis Clube': ['TwoDrive', 'Tijuca_Tênis_Clube'],
            'Museu da Republica no Catete': ['ThreeDrive', 'Museu_da_República_Catete'],
            'Paroquia Nossa Senhorado Rosario no Leme': ['FourDrive', 'Paróquia_Nossa_Senhora_do_Rosário_Leme'],
            'Casa Firjan Botafogo': ['FiveDrive', 'Casa_Firjan_Botafogo'],
            'Jockey Club Brasileiro Gavea': ['SixDrive', 'Jockey_Club_Brasileiro_Gávea'],
            'Hotel Fairmont em Copacabana': ['SevenDrive', 'Hotel_Fairmont_Copacabana'],
            'Museu da Justiça no Centro': ['EightDrive', 'Museu_da_Justiça_Centro'],
            'Cidade_das_Artes_Barra_da_Tijuca': ['NineDrive', 'Cidade_das_Artes_Barra_da_Tijuca'],
            'Quartéis do Corpo de Bombeiros Humaitá': ['TenDrive', 'Quartéis_do_Corpo_de_Bombeiros_Humaitá'],
            'Quartéis do Corpo de Bombeiros Copacabana': ['ElevenDrive', 'Quartéis_do_Corpo_de_Bombeiros_Copacabana'],
            'Quartel de Busca e Salvamento Barra da Tijuca': ['TwelveDrive', 'Quartel_de_Busca_e_Salvamento_Barra_da_Tijuca'],
            'Museu do Amanhã Centro': ['ThirteenDrive', 'Museu_do_Amanhã_Centro']}


PlanetarioDaGavea = ['Rua Vice-Governador Rúbens Berardo, 100 - Gávea, Rio de Janeiro - RJ, 22451-070',
                         'Segunda a Sexta: das 8 às 17 horas',
                         '-22.977951036479063',
                         '-43.230301869393136',
                         '(21) 2088-0539']

TijucaTenisClube = ['Rua Conde de Bonfim, 451 - Tijuca, Rio de Janeiro - RJ, 20520-054',
                    'Segunda a Sexta: das 8 às 17 horas',
                    '-22.92715413115991',
                    '-43.23475129326639',
                    '(21) 3294-9300']

MuseuDaRepublicaCatete = ['Palácio do Catete. Rua do Catete 153, Catete - RJ. cep 22220-000',
                          'Segunda a Sexta: das 8 às 15 horas',
                          '-22.92585796484139',
                          '-43.176321953629795',
                          '(21) 2127-0324']

ParoquiaNossaSenhoradoRosarioLeme = ['Rua General Ribeiro da Costa, 164 - Leme, Rio de Janeiro - RJ, 22010-050',
                                     'Segunda a Sexta: das 8 às 12 horas',
                                     '-22.961998176549486',
                                     '-43.16975685013149',
                                     '(21) 3042-2792']

CasaFirjanBotafogo = ['R. Guilhermina Guinle, 211 - Botafogo, Rio de Janeiro - RJ, 22260-001',
                        'Segunda a Sexta: das 8 às 17 horas',
                        '-22.950105691328655',
                        '-43.18896962268458',
                        '0800 023 1231']

JockeyClubBrasileiroGavea = ['Praça Santos Dumont, 31 - Gávea, Rio de Janeiro - RJ, 22470-060',
    'Segunda a Sexta: das 8 às 15 horas',
                             '-22.97375365559369', '-43.2249067909956',
                             '(21) 3534-9061']

HotelFairmontCopacabana = ['Av. Atlântica, 4240 - Copacabana, Rio de Janeiro - RJ, 22070-002',
                           'Segunda a Sexta: das 8 às 17 horas',
'-22.986444642275597', '-43.189475907984324',
                           '(21) 2525-1232']

MuseudaJusticaCentro = ['R. Dom Manuel, 29 - térreo - Centro, Rio de Janeiro - RJ, 20010-090',
                        'Segunda a Sexta: das 8 às 17 horas',
                        '-22.904681968771968', '-43.17261345830698',
                        '(21) 2524-5817']

CidadedasArtesBarradaTijuca = ['Av. das Américas, 5300 - Barra da Tijuca, Rio de Janeiro - RJ, 22793-080',
                               'Segunda a Sexta: das 8 às 17 horas',
                               '-22.99914612400007', '-43.36579357670063',
                               '(21) 3325-0102']

QuarteisdoCorpodeBombeirosHumaita = ['Rua Humaitá, 126 - Humaitá, Rio de Janeiro - RJ, 22261-001',
                                     'Segunda a Sexta: das 8 às 12 horas',
                                     '-22.957499646448177', '-43.199273528161676',
                                     '(21) 2332-1538']

QuarteisdoCorpodeBombeirosCopacabana = ['R. Xavier da Silveira, 120 - Copacabana, Rio de Janeiro - RJ, 22061-020',
                                        'Segunda a Sexta: das 8 às 12 horas',
'-22.976059550350865', '-43.19344520737091','(21) 2333-8669']

QuarteldeBuscaeSalvamentoBarradaTijuca = ['Av. Ayrton Senna, 2001 - Jacarepaguá, Rio de Janeiro - RJ, 22775-002',
                                          'Segunda a Sexta: das 8 às 12 horas',
                                          '-22.99201882973034', '-43.368879906764555',
                                          '(21) 2333-4404']

MuseudoAmanhaCentro = ['Praça Mauá, 1 - Centro, Rio de Janeiro - RJ, 20081-240',
                       'Segunda a Sexta: das 8 às 17 horas', '-22.894330536276694', '-43.17945998037699',
                       '(21) 3812-1800']

ImperatorMeier = ['R. Dias da Cruz, 170 - Méier, Rio de Janeiro - RJ, 20720-012',
                  'Segunda a Sexta: das 8 às 17 horas', '-22.90263485616673', '-43.28200595896241','(21) 2597-3897']

QuadradoCaciquedeRamosOlaria = ['R. Uranos, 1326 - Olaria, Rio de Janeiro - RJ, 21060-070',
                                'Sábado: das 8 às 17 horas','-22.849581895132665', '-43.265261729503976',
                                '(21) 3251-4374']

VilaMilitarDeodoro = ['Estr. São Pedro de Alcântara, 2020 - Vila Militar, Rio de Janeiro - RJ, 21615-435',
                      'Sábado: das 8 às 17 horas',
                      '-22.86118170898703', '-43.401649499370095','(21) 98345-0200']

MuseuCondedeLinharesSaoCristovao = ['Av. Pedro II, 383 - São Cristóvão, Rio de Janeiro - RJ, 20941-070',
                                         'horario',
                                         '-22.90490468228338', '-43.21921780004544',
                                         '(21) 2589-9581', ]
ClubMunicipalTijuca = ['R. Haddock Lobo, 359 - Tijuca, Rio de Janeiro - RJ, 20260-130',
                       'horario', '-22.921058520821436', '-43.217686850707366', '(21) 2569-4822']

PalacioDuquedeCaxiasCentro = ['Praça Duque de Caxias, 25 - Centro, Rio de Janeiro - RJ, 20221-260',
                              'horario', '-22.903322787007856', '-43.189717941290944', '(21) 2519-5000']

QuadradaPortelaMadureira = ['R. Clara Nunes, 81 - Oswaldo Cruz, Rio de Janeiro - RJ, 21351-110', 'horario',
                            '-22.87099937474735', '-43.3429253316898', '(21) 3217-1604']

EspacoCulturaldaMarinhaCentro = ['Boulevard Olímpico, Praça XV Centro, Túnel Pref. Marcello Alencar, Rio de Janeiro - RJ, 20040-010',
                                 'horario', '-22.90044317872919', '-43.17473135622443', '(21) 2532-5992']

CentrodeInstrucaoAlmiranteMilciadesPortelaAlvesCIAMPACampoGrande = ['Praça Mauá, 1 - Centro, Rio de Janeiro - RJ, 20081-240',
                                                                    'horario', '-22.89397511898424', '-43.17939033966276',
                                                                    '(21) 3812-1800']

BaseAereadoGaleaoIlhadoGovernador = ['Estrada do Galeão, s/n - Ilha do Governador, Rio de Janeiro - RJ, 21941-005',
                                     'horario', '-22.82379167106415', '-43.2331699324818', '(21) 2138-4184']

UERJMaracanaportao1 = ['R. São Francisco Xavier, 524 - Maracanã, Rio de Janeiro - RJ, 20550-013', 'horario',
                       '-22.91115844362454', '-43.23611889121059', '(21) 2334-0000']

ConselhoRegionaldeEnfermagemdoRiodeJaneiroCorenRJCentro = ['502 3º, 4º 5º e 6º andares, Av. Pres. Vargas - Centro, Rio de Janeiro - RJ, 20071-000',
                                                           'horario', '-22.90130842471268', '-43.18053661902731',
                                                           '(21) 3232-8730']

ConselhoRegionaldeFarmaciaTijuca = ['R. Afonso Pena, 115 - Tijuca, Rio de Janeiro - RJ, 20270-244',
                                    'horario', '-22.917074309049838', '-43.219200518803035', '(21) 3872-9200']

ABBRJardimBotanico = ['R. Jardim Botânico, 660 - Jardim Botânico, Rio de Janeiro - RJ, 22461-000', 'horario',
                      '-22.964250471509096', '-43.218324261144616', '(21) 3528-6363']

ParqueOlimpicoBarradaTijuca = ['Av. Embaixador Abelardo Bueno, 3401 - Barra da Tijuca, Rio de Janeiro - RJ, 22775-040',
                               'horario', '-22.973903444465876', '-43.393615383073616', '...']

SambodromoSantoCristo = ['R. Marquês de Sapucaí - Santo Cristo, Rio de Janeiro - RJ, 20220-007',
                         'horario', '-22.91143243515152', '-43.196771142923986', '(21) 2976-7310']

MuseuAeroespacialCampodosAfonsos = ['Av. Marechal Fontenele, 2000 - Campo dos Afonsos, Rio de Janeiro - RJ, 21740-000',
                                    'horario', '-22.885025720164766', '-43.39052303730502', '(21) 2157-2899']

postos = ['', PlanetarioDaGavea, TijucaTenisClube, MuseuDaRepublicaCatete,
          ParoquiaNossaSenhoradoRosarioLeme, CasaFirjanBotafogo, JockeyClubBrasileiroGavea, HotelFairmontCopacabana,
          MuseudaJusticaCentro, CidadedasArtesBarradaTijuca, QuarteisdoCorpodeBombeirosHumaita,
          QuarteisdoCorpodeBombeirosCopacabana, QuarteldeBuscaeSalvamentoBarradaTijuca, MuseudoAmanhaCentro,
          ImperatorMeier, QuadradoCaciquedeRamosOlaria, VilaMilitarDeodoro, MuseuCondedeLinharesSaoCristovao,
          ClubMunicipalTijuca, PalacioDuquedeCaxiasCentro, QuadradaPortelaMadureira, EspacoCulturaldaMarinhaCentro,
          CentrodeInstrucaoAlmiranteMilciadesPortelaAlvesCIAMPACampoGrande, BaseAereadoGaleaoIlhadoGovernador,
          UERJMaracanaportao1, ConselhoRegionaldeEnfermagemdoRiodeJaneiroCorenRJCentro, ConselhoRegionaldeFarmaciaTijuca,
          ABBRJardimBotanico, ParqueOlimpicoBarradaTijuca, SambodromoSantoCristo, MuseuAeroespacialCampodosAfonsos]

postosTabelas = ['Escolha_um_posto_de_vacinação', 'Planetário_da_Gávea', 'Tijuca_Tênis_Clube', 'Museu_da_República_Catete', 'Paróquia_Nossa_Senhora_do_Rosário_Leme',
           'Casa_Firjan_Botafogo', 'Jockey_Club_Brasileiro_Gávea',
          'Hotel_Fairmont_Copacabana', 'Museu_da_Justiça_Centro', 'Cidade_das_Artes_Barra_da_Tijuca',
          'Quartéis_do_Corpo_de_Bombeiros_Humaitá','Quartéis_do_Corpo_de_Bombeiros_Copacabana','Quartel_de_Busca_e_Salvamento_Barra_da_Tijuca',
          'Museu_do_Amanhã_Centro', 'Imperator_Méier', 'Quadra_do_Cacique_de_Ramos_Olaria',
          'Vila_Militar_Deodoro', 'Museu_Conde_de_Linhares_São_Cristóvão', 'Club_Municipal_Tijuca',
          'Palácio_Duque_de_Caxias_Centro', 'Quadra_da_Portela_Madureira', 'Espaço_Cultural_da_Marinha_Centro',
          'Centro_de_Instrução_Almirante_Milcíades_Portela_Alves_CIAMPA_Campo_Grande', 'Base_Aérea_do_Galeão_Ilha_do_Governador',
          'UERJ_Maracanã_portão_1', 'Conselho_Regional_de_Enfermagem_do_Rio_de_Janeiro_Coren_RJ_Centro',
          'Conselho_Regional_de_Farmácia_Tijuca', 'ABBR_Jardim_Botânico','Parque_Olímpico_Barra_da_Tijuca',
          'Sambódromo_Santo_Cristo', 'Museu_Aeroespacial_Campo_dos_Afonsos']


postosDisplay = ['Escolha um posto de vacinação', 'Planetário da Gávea', 'Tijuca Tênis Clube', 'Museu da República (Catete)', 'Paróquia Nossa Senhora do Rosário (Leme)',
           'Casa Firjan (Botafogo)', 'Jockey Club Brasileiro (Gávea)',
          'Hotel Fairmont (Copacabana)', 'Museu da Justiça (Centro)', 'Cidade das Artes (Barra da Tijuca)',
          'Quartéis do Corpo de Bombeiros: Humaitá, Copacabana e Quartel de Busca e Salvamento (Barra da Tijuca)',
          'Museu do Amanhã (Centro)', 'Imperator (Méier)', 'Quadra do Cacique de Ramos (Olaria)',
          'Vila Militar (Deodoro)', 'Museu Conde de Linhares (São Cristóvão)', 'Club Municipal (Tijuca)',
          'Palácio Duque de Caxias (Centro)', 'Quadra da Portela (Madureira)', 'Espaço Cultural da Marinha (Centro)',
          'Centro de Instrução Almirante Milcíades Portela Alves (CIAMPA – Campo Grande)', 'Base Aérea do Galeão (Ilha do Governador)',
          'UERJ (Maracanã) portão 1', 'Conselho Regional de Enfermagem do Rio de Janeiro Coren-RJ (Centro)',
          'Conselho Regional de Farmácia (Tijuca)', 'ABBR (Jardim Botânico)', 'Parque Olímpico (Barra da Tijuca)',
                 'Sambódromo (Santo Cristo)', 'Museu Aeroespacial (Campo dos Afonsos)']

funcionamentoTabelas = ['Todos_os_dias', 'Segunda_a_sexta', 'Sábado', 'Sábado_domingo_e_feriados', 'Feriados',
                       'Sábado_e_domingo', 'Segunda_e_terça', 'Segunda_a_quarta', 'Segunda_a_quinta',
                       'Terça_e_quarta', 'Terça_a_quinta', 'Terça_a_Sexta', 'Quarta_e_quinta', 'Quarta_a_sexta',
                       'Quinta_e_sexta']

funcionamentoDisplay = ['Todos os dias', 'Segunda a sexta', 'Sábado', 'Sábado, domingo e feriados', 'Feriados',
                       'Sábado e domingo', 'Segunda e terça', 'Segunda a quarta', 'Segunda a quinta',
                       'Terça e quarta', 'Terça a quinta', 'Terça a Sexta', 'Quarta e quinta', 'Quarta a sexta',
                       'Quinta e sexta']

ql_hk12.title('Estoque de Vacinas no Rio de Janeiro')
postoSelecionado = ql_hk12.selectbox('Selecione um posto de vacinação para saber quantas vacinas estão disponíveis', postosDisplay)

sidebar = ql_hk12.beta_container()
with sidebar:
    ql_hk12.sidebar.header('Posto')
    postoNome = ql_hk12.sidebar.text('Escolha um posto de vacinação ao lado')
    ql_hk12.sidebar.header('Número de Vacinas disponíveis')
    vacinasDisplay = ql_hk12.sidebar.text('...')
    ql_hk12.sidebar.subheader('Endereço')
    endereco = ql_hk12.sidebar.text('...')
    ql_hk12.sidebar.subheader('Horário de Funcionamento')
    horario = ql_hk12.sidebar.text('...')
    ql_hk12.sidebar.subheader('Telefone')
    telefone = ql_hk12.sidebar.text('...')
    latitude = -22.911457737201688
    longitude = -43.209697383676245
    zoomInicial = 13

if postoSelecionado != postosDisplay[0]:
    indice1 = postosDisplay.index(postoSelecionado)
    postoEnderecoSelecionado = postos[indice1][0]
    postoHorarioSelecionado = postos[indice1][1]
    postoLatitudeSelecionado = postos[indice1][2]
    postoLongitudeSelecionado = postos[indice1][3]
    postoTelefoneSelecionado = postos[indice1][4]
    postoNome.text(body=postoSelecionado)

    if retrieve_vac(postosTabelas[indice1], strftime("%Y", gmtime()), strftime("%m", gmtime()), strftime("%d", gmtime())) != []:
        vacinasDisplay.text(body=retrieve_vac(postosTabelas[indice1], strftime("%Y", gmtime()), strftime("%m", gmtime()), strftime("%d", gmtime())))
    if retrieve_horario(postosTabelas[indice1], strftime("%Y", gmtime()), strftime("%m", gmtime()), strftime("%d", gmtime())) != []:
        horario.text(body=retrieve_horario(postosTabelas[indice1], strftime("%Y", gmtime()), strftime("%m", gmtime()), strftime("%d", gmtime())))
    endereco.text(body=postoEnderecoSelecionado)
    telefone.text(body=postoTelefoneSelecionado)
    latitude = postoLatitudeSelecionado
    longitude = postoLongitudeSelecionado
    zoomInicial = 20

ma1k7_89 = a1k7_89.Map(location=[latitude, longitude], zoom_start=zoomInicial)
a1k7_89.Marker(location=[latitude, longitude], popup=postoSelecionado, tooltip='Clique aqui').add_to(ma1k7_89)
folium_static(ma1k7_89, width=800, height=600)

ql_hk12.title('Seção destinada aos administradores da saúde pública')
with ql_hk12.form('Form2'):
    col1, col2 = ql_hk12.beta_columns(2)
    userLogin = col1.text_input('Digite seu login')
    userSenha = col2.text_input('Digite sua senha', type='password')
    numVacinas = ql_hk12.text_input('Digite a quantidade de vacinas disponíveis')
    ql_hk12.subheader('Informe o horário de funcionamento')
    horarioInicial = col1.text_input('Horário de Abertura')
    horarioFinal = col2.text_input('Horário de Fechamento')
    diaSelecionado = ql_hk12.selectbox('Selecione o dia(s) de funcionamento', funcionamentoDisplay)
    submit = ql_hk12.form_submit_button('Atualizar')

if submit:
    if userLogin in dictAuth.keys() and userSenha == dictAuth[userLogin][0]:
        if filtroVac(numVacinas):
            add_vac(dictAuth[userLogin][1], numVacinas, strftime("%Y", gmtime()), strftime("%m", gmtime()), strftime("%d", gmtime()))
            ql_hk12.success('Informação sobre vacinas disponíveis adicionada com sucesso')
        elif numVacinas == '':
            ql_hk12.warning('Nenhuma informação sobre a quantidade de vacinas foi adicionada')
        else:
            ql_hk12.error('Informe o número de vacinas disponível corretamento')
        if filtroHoras(horarioInicial) and filtroHoras(horarioFinal):
            add_horario(dictAuth[userLogin][1], diaSelecionado, horarioInicial, horarioFinal, strftime("%Y", gmtime()), strftime("%m", gmtime()), strftime("%d", gmtime()))
            ql_hk12.success('Informação sobre o horário inicial e final de vacinação adicionada com sucesso')
        elif horarioInicial == '' or horarioFinal == '':
            ql_hk12.warning('Informações sobre o horário inicial e final de vacinação estão incompleto')
        else:
            ql_hk12.error('Informe corretamente o horário inicial e final de vacinação')
    else:
        sleep(3)
        ql_hk12.error('Login ou Senha Inválidos/Contate o administrador para resolução')
