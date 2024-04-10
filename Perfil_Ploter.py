import os

from pycatia import catia
from pycatia.mec_mod_interfaces.part import Part
from pycatia.mec_mod_interfaces.part_document import PartDocument
from pycatia.scripts.csv_tools import create_points



nome = input("Digite o nome do arquivo csv DA FORMA COMO ESTÁ ESCRITO, \nPREFERÊNCIALMENTE SEM ESPAÇOS E SEM O FINAL '.csv': ")
os.system('cls')
validador = input(f"Deseja Confirmar '{nome}.csv' como o nome do arquivo? (S/N): ")
os.system('cls')

while validador.lower() != 's':

    nome = input(
        "Digite o nome do arquivo csv DA FORMA COMO ESTÁ ESCRITO, \nPREFERÊNCIALMENTE SEM ESPAÇOS E SEM O FINAL '.csv': ")
    os.system('cls')

    validador = input(f"Deseja Confirmar '{nome}.csv' como o nome do arquivo? (S/N): ")
    os.system('cls')

pass

caa = catia()

documents = caa.documents

documents.add("Part")

document = PartDocument(caa.active_document.com_object)
part = Part(document.part.com_object)

file = fr"Arquivo_csv\{nome}.csv"

create_points(part, file, units="mm", geometry_set_name="Perfil_Aerodinamico")

os.system('cls')
input("Processo concluído, para sair tecle Enter: ")
