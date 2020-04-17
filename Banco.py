import pymysql

# Inicializa o servidor
cone = pymysql.connect(host="localhost", user="root", passwd="", database="votingsystembd")
cursor = cone.cursor()


# Salva o banco
def commit():
    cone.commit()


# Insere eleitor no banco de dados sem repetição
def inserir_eleitor_bd(eleitor):
    args = (eleitor.get_nome(), eleitor.get_idade(), eleitor.get_cpf(), eleitor.get_sexo(), eleitor.get_titulo())
    cursor.execute("INSERT IGNORE INTO eleitor(nome, idade, cpf, sexo, titulo) VALUES (%s, %s, %s, %s, %s);", args)
    commit()


# Deleta eleitor do banco de dados de acordo com o CPF
def deletar_eleitor_bd(cpf):
    cursor.execute("DELETE FROM eleitor WHERE cpf = %s", cpf)
    commit()


# Retorna os eleitores do banco de Dados
def eleitores_bd():
    cursor.execute("SELECT * FROM `eleitor`")
    return list(cursor)


# Insere candidato no banco de dados sem repetição
def inserir_candidato_bd(candidato):
    args = (
    candidato.get_nome(), candidato.get_idade(), candidato.get_cpf(), candidato.get_sexo(), candidato.get_titulo(),
    candidato.get_id_candidato())
    cursor.execute(
        "INSERT IGNORE INTO candidato(nome, idade, cpf, sexo, titulo, id_candidato) VALUES (%s, %s, %s, %s, %s, %s);",
        args)
    commit()


# Deleta candidato do banco de dados de acordo com o ID do eleitor
def deletar_candidato_bd(id_candidato):
    cursor.execute("DELETE FROM candidato WHERE id_candidato = %s", id_candidato)
    commit()


# Retorna os candidatos do banco de dados
def candidatos_bd():
    cursor.execute("SELECT * FROM `candidato`")
    return list(cursor)

def resetar_a_i():
    cursor.execute("ALTER TABLE candidato AUTO_INCREMENT = 1")