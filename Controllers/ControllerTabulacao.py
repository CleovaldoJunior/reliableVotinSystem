def buscar_candidato(n_candidato, lista_candidatos):
    for candidato in lista_candidatos:
        if candidato.get_n_candidato() == n_candidato:
            return candidato