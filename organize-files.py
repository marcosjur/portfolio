"Criated by Marcos Barboza"
"File Organizer"

#---imports---#
import os
import glob
import shutil
import os.path
import time
from pathlib import Path

user_type = input("Insira o formato: ")
user_source = input("Insira a origem: ")
user_destination = input("Insira o destino: ")

#---move---#
escape_not = ('\\')
file_type_name = user_type
file_type_extention = '*.'+file_type_name # Cria o modelo de extenção de arquivo
source_directory = r'C:\Users\marco'+str(escape_not)+user_source+str(escape_not) # Origem do arquivo
destiny_directory = r'D:\Biblioteca'+str(escape_not)+user_destination # Destino do arquivo
destiny_directory_create = destiny_directory + str(escape_not) + file_type_name # Destino para criar pasta
os.system('cls')

def file_organize(source_directory, destiny_directory, file_type_extention, file_type_name,destiny_directory_create):
    
    list_executable = glob.glob(file_type_extention) # Procura pela extenção de arquivo fornecida
    print('file in directory: '+str(len(list_executable))) # Exibe a quantidade de arquivos encontrados
    if len(list_executable) >= 1: # Valida se existe arquivos da extenção especificada
        if not os.path.exists(destiny_directory): # Verifica a existencia de pasta para a extenção 
            os.mkdir(destiny_directory_create)
            print('Pasta de Executáveis Criada!')

        for file in list_executable:
            file_name = file
            shutil.move(os.path.join(source_directory, file),os.path.join(destiny_directory, file))
            print(f'File: "{file_name}" in -- {source_directory} -- has be moved to ->> {destiny_directory}')
    else:
        os.system('cls')
        print(f'The directory {source_directory} is empty!')
        time.sleep(5)

if __name__ == '__main__':
    file_organize(source_directory,destiny_directory,file_type_extention,file_type_name,destiny_directory_create)
