import pymysql

cone = pymysql.connect(host="localhost", user="root", passwd="", database="votingsystembd")
cursor = cone.cursor()


def inserir_eleitor_banco(eleitor):
    args = (eleitor.get_nome(), eleitor.get_idade(), eleitor.get_cpf(), eleitor.get_sexo(), eleitor.get_titulo())
    cursor.execute("INSERT INTO eleitor(nome, idade, cpf, sexo, titulo) VALUES (%s, %s, %s, %s, %s)", args)
    cone.commit()

cursor.execute("SELECT * FROM `eleitor`")
for i in cursor:
    print(i)

