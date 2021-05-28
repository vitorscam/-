import sqlite3 as sq

def filtroHoras(horas):
    if horas.isnumeric() and 0 <= int(horas) <= 24:
        return True
    else:
        return False

def filtroVac(vacinas):
    if vacinas.isnumeric() and int(vacinas) >= 0:
        return True
    else:
        return False

def retrieve_horario(tabela, ano, mes, dia):
    con = sq.connect('horarios.db')
    cur = con.cursor()
    cur.execute(f'SELECT * FROM {tabela} WHERE Ano={ano} AND Mes={mes} AND Dia={dia};')
    consulta = cur.fetchall()
    con.close()
    if consulta != []:
        return f'{consulta[-1][1]}: das {consulta[-1][2]} às {consulta[-1][3]} horas'
    return '...'

def retrieve_vac(tabela, ano, mes, dia):
    con = sq.connect('base.db')
    cur = con.cursor()
    cur.execute(f'SELECT * FROM {tabela} WHERE Ano={ano} AND Mes={mes} AND Dia={dia};')
    consulta = cur.fetchall()
    con.close()
    if consulta != []:
        return f'Vacinas disponíveis: {consulta[-1][1]}\nNa data: {consulta[-1][4]}/{consulta[-1][3]}/{consulta[-1][2]}'
    return '...'

def add_horario(tabela, diaSel, horarioinicio, horariofim, ano, mes, dia):
    con = sq.connect('horarios.db')
    cur = con.cursor()
    cur.execute(f'INSERT INTO {tabela}(DiaSel, HorarioInicial, HorarioFinal, Ano, Mes, Dia) VALUES("{diaSel}", {horarioinicio}, {horariofim}, {ano}, {mes}, {dia})')
    con.commit()
    con.close()


def add_vac(tabela, numeroVacinas, ano, mes, dia):
    con = sq.connect('base.db')
    cur = con.cursor()
    cur.execute(f'INSERT INTO {tabela}(Vacinas, Ano, Mes, Dia) VALUES({numeroVacinas}, {ano}, {mes}, {dia})')
    con.commit()
    con.close()


'''
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


for nomes in postosTabelas:
    con = sq.connect('horarios.db')
    cur = con.cursor()
    cur.execute(f"CREATE TABLE {nomes}(ID INTEGER PRIMARY KEY AUTOINCREMENT, DiaSel TEXT, HorarioInicial TEXT, HorarioFinal TEXT, Ano TEXT, Mes TEXT, Dia TEXT)")
    #cur.execute(f"CREATE TABLE {nomes}(ID INTEGER PRIMARY KEY AUTOINCREMENT, Vacinas TEXT, Ano TEXT, Mes TEXT, Dia TEXT)")
    con.commit()
    con.close()'''