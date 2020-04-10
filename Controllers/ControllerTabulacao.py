def buscar_candidato(n_candidato, lista_candidatos):
    for i in lista_candidatos:
        if i.get_n_candidato() == n_candidato:
            return i