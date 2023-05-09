import zipfile
import datetime
import os
import locale
import configparser
import re

# Establecer la configuración regional en español
locale.setlocale(locale.LC_TIME,'es_ES.UTF-8')

# Leer el archivo de configuración
config = configparser.ConfigParser()
config.read('config.ini')

# Pedir usuario y fichero
name = input("Introduce el nombre de la persona\n").lower()
file = input("Introduce el nombre del archivo sin extension\n") + '.ZIP'

if name == 'anthony':
    # Obtener la variable output_directory del archivo de configuración
    output_directory = config.get('anthony', 'output_directory')
    # Obtener la variable password del archivo de configuración
    password = config.get('anthony', 'password')
elif name == 'mariale':
    output_directory = config.get('mariale', 'output_directory')
    password = config.get('mariale', 'password')

with zipfile.ZipFile(config.get('default', 'directory')+file) as file_zip:
    file_zip.setpassword(password.encode())
    file_zip.extractall(output_directory)
    for filename in file_zip.namelist():
        # Obtener la fecha actual
        actual_date = datetime.datetime.now().strftime("%Y_%B - ").upper()
        # Separar el nombre del archivo y su extensión
        file_name, extension = os.path.splitext(filename)
        # Buscar la primera aparición de una letra en el nombre del archivo
        primer_letra = re.search("[a-zA-Z]", file_name)
        # Eliminar los caracteres anteriores a la primera aparición de una letra
        name_without_numbers = file_name[primer_letra.start():]
        # Establecer la cadena del nombre nuevo
        new_name = actual_date +name_without_numbers+ os.path.splitext(filename)[1]
        # Renombrar el archivo
        os.rename(os.path.join(output_directory, filename), os.path.join(output_directory, new_name))
    
print("Creado el archivo",new_name)