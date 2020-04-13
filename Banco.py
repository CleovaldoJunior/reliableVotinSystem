import pymysql

cone = pymysql.connect(host="localhost", user="root", passwd="", database="votingsystembd")
cursor = cone.cursor()

def commit():
    cone.commit()

def inserir_eleitor_bd(eleitor):
    args = (eleitor.get_nome(), eleitor.get_idade(), eleitor.get_cpf(), eleitor.get_sexo(), eleitor.get_titulo())
    cursor.execute("INSERT IGNORE INTO eleitor(nome, idade, cpf, sexo, titulo) VALUES (%s, %s, %s, %s, %s)", args)
    commit()

def deletar_eleitor_bd(cpf):
    cursor.execute("DELETE FROM eleitor WHERE cpf = %s", cpf)
    commit()

def eleitores_bd():
    cursor.execute("SELECT * FROM `eleitor`")
    return list(cursor)