grafo = {
    'ESTADIO_NACIONAL_DO_ZIMPETO': [('NKOBE', 14), ('FACULDADE_DE_ENGENHARIA_UEM', 15)],
    'NKOBE': [('MACHAVA_KM15', 6), ('PATRICE_LUMUMBA', 10), ('ESTADIO_NACIONAL_DO_ZIMPETO', 14)],
    'FACULDADE_DE_ENGENHARIA_UEM': [('ESTADIO_DA_MACHAVA', 6), ('PORTAGEM_MP_MC', 7), ('UEM_CAMPUS', 8), ('MAGOANINE', 12), ('MUSEU_DOS_CFM', 15), ('ESTADIO_NACIONAL_DO_ZIMPETO', 15)],
    'MACHAVA_KM15': [('SOCIMOL', 1), ('NKOBE', 6)],
    'PATRICE_LUMUMBA': [('ESTADIO_DA_MACHAVA', 4), ('NKOBE', 10)],
    'ESTADIO_DA_MACHAVA': [('PATRICE_LUMUMBA', 4), ('FACULDADE_DE_ENGENHARIA_UEM', 6), ('SOCIMOL', 14)],
    'PORTAGEM_MP_MC': [('FACULDADE_DE_ENGENHARIA_UEM', 7), ('SOCIMOL', 11), ('AIROPORTO', 11), ('UEM_CAMPUS', 16)],
    'UEM_CAMPUS': [('PRACA_DOS_COMBATENTES', 4), ('HCM', 5), ('MAPUTO_SHOPPING', 5), ('PRAIA_DE_COSTA_DE_SOL', 7), ('FACULDADE_DE_ENGENHARIA_UEM', 8), ('PORTAGEM_MP_MC', 16)],
    'MAGOANINE': [('AIROPORTO', 11), ('FACULDADE_DE_ENGENHARIA_UEM', 12)],
    'MUSEU_DOS_CFM': [('HCM', 3), ('PRACA_DOS_COMBATENTES', 8), ('FACULDADE_DE_ENGENHARIA_UEM', 15)],
    'SOCIMOL': [('MACHAVA_KM15', 1), ('PORTAGEM_MP_MC', 11), ('ESTADIO_DA_MACHAVA', 14), ('HCM', 18)],
    'AIROPORTO': [('PRACA_DOS_COMBATENTES', 5), ('MAGOANINE', 11), ('PORTAGEM_MP_MC', 11)],
    'PRACA_DOS_COMBATENTES': [('UEM_CAMPUS', 4), ('AIROPORTO', 5), ('MUSEU_DOS_CFM', 8)],
    'HCM': [('MUSEU_DOS_CFM', 3), ('UEM_CAMPUS', 5), ('SOCIMOL', 18)],
    'MAPUTO_SHOPPING': [('MUSEU_DE_HISTORIA_NATURAL', 1), ('UEM_CAMPUS', 5)],
    'PRAIA_DE_COSTA_DE_SOL': [('UEM_CAMPUS', 7)],
    'MUSEU_DE_HISTORIA_NATURAL': [('MAPUTO_SHOPPING', 1)],
}

def custo_caminho(caminho):
    custo_total = 0
    for (no, custo) in caminho:
        custo_total += custo
    return custo_total, caminho[-1][0]


def ucs(grafo, origem, objectivo):
    visitado = []
    fila = [[(origem, 0)]]

    while fila:
        # ordenando pelo custo
        fila.sort(key=custo_caminho)
        # Escolhendo o menor custo
        caminho = fila.pop(0)

        no = caminho[-1][0]

        if no in visitado:
            continue
        visitado.append(no)

        if no == objectivo:
            return caminho
        else:
            nos_adjacentes = grafo.get(no, [])

            for (no_2, custo) in nos_adjacentes:
                novo_caminho = caminho.copy()
                novo_caminho.append((no_2, custo))
                fila.append(novo_caminho)


def main():
    origem = escolher_local("ORIGEM")
    if origem is None:
        return

    destino = escolher_local("DESTINO")
    if destino is None:
        return

    solucao_otima = ucs(grafo, origem, destino)
    print("\n" + "*" * 100)
    print(f'Solução ótima é: {solucao_otima}')
    print(f'O custo da solução é: {custo_caminho(solucao_otima)[0]}')
    print("\n" + "*" * 100)



def escolher_local(local_nome):
    print("*" * 20 + f" {local_nome} " + "*" * 20)
    print("1 - ESTADIO_NACIONAL_DO_ZIMPETO")
    print("2 - NKOBE")
    print("3 - FACULDADE_DE_ENGENHARIA_UEM")
    print("4 - MACHAVA_KM15")
    print("5 - PATRICE_LUMUMBA")
    print("6 - ESTADIO_DA_MACHAVA")
    print("7 - PORTAGEM_MP_MC")
    print("8 - UEM_CAMPUS")
    print("9 - MAGOANINE")
    print("10 - MUSEU_DOS_CFM")
    print("11 - SOCIMOL")
    print("12 - AIROPORTO")
    print("13 - PRACA_DOS_COMBATENTES")
    print("14 - HCM")
    print("15 - MAPUTO_SHOPPING")
    print("16 - PRAIA_DE_COSTA_DE_SOL")
    print("17 - MUSEU_DE_HISTORIA_NATURAL")
    print("*" * 25)
    opcao = int(input(f"Digite o número correspondente ao ponto {local_nome}: "))
    print("\n\n")

    locais = {
        1: 'ESTADIO_NACIONAL_DO_ZIMPETO',
        2: 'NKOBE',
        3: 'FACULDADE_DE_ENGENHARIA_UEM',
        4: 'MACHAVA_KM15',
        5: 'PATRICE_LUMUMBA',
        6: 'ESTADIO_DA_MACHAVA',
        7: 'PORTAGEM_MP_MC',
        8: 'UEM_CAMPUS',
        9: 'MAGOANINE',
        10: 'MUSEU_DOS_CFM',
        11: 'SOCIMOL',
        12: 'AIROPORTO',
        13: 'PRACA_DOS_COMBATENTES',
        14: 'HCM',
        15: 'MAPUTO_SHOPPING',
        16: 'PRAIA_DE_COSTA_DE_SOL',
        17: 'MUSEU_DE_HISTORIA_NATURAL',
    }

    if opcao in locais:
        return locais[opcao]
    else:
        print(f"{local_nome} inválido")
        return None


main()
