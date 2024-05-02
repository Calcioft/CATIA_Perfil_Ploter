import os

from pycatia import catia
from pycatia.mec_mod_interfaces.part import Part
from pycatia.mec_mod_interfaces.part_document import PartDocument
from pycatia.scripts.csv_tools import create_points
n = 1
i = 0

quantidade = int(input(f"Digite a quantidade de perfis que você deseja plotar:"))
lista_nomes = []

while n <= quantidade:

    nome = input(f"Digite o nome do arquivo csv de número '{n}' DA FORMA COMO ESTÁ ESCRITO, \nPREFERÊNCIALMENTE SEM ESPAÇOS E SEM O FINAL '.csv': ")
    validador = input(f"Deseja Confirmar '{nome}.csv' como o nome do arquivo? (S/N): ")
    os.system('cls')

    while validador.lower() != 's':
        nome = input(
            "Digite o nome do arquivo csv DA FORMA COMO ESTÁ ESCRITO, \nPREFERÊNCIALMENTE SEM ESPAÇOS E SEM O FINAL '.csv': ")
        os.system('cls')

        validador = input(f"Deseja Confirmar '{nome}.csv' como o nome do arquivo? (S/N): ")
        os.system('cls')

    pass
    lista_nomes.append(nome)
    n = n+1

os.system('cls')

print(f"Imprimindo arquivos '{lista_nomes}'")



caa = catia()

documents = caa.documents

documents.add("Part")

document = PartDocument(caa.active_document.com_object)
part = Part(document.part.com_object)

while i <= quantidade-1:

    file = fr"Arquivo_csv\{lista_nomes[i]}.csv"

    create_points(part, file, units="mm", geometry_set_name=f"Perfil_Aerodinamico{i}")

    i = i + 1

    os.system('cls')
input("Processo concluído, para sair tecle Enter: ")
