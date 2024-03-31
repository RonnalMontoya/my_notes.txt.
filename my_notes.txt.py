# Escritura de Archivo de Texto
# Creamos un nuevo archivo llamado my_notes.txt en modo de escritura 
with open('my_notes.txt', 'w') as file:
    # Escribimos al menos tres líneas de notas personales en el archivo
    file.write("Notas Personales:\n")
    file.write("- Recordar ir al médico.\n")
    file.write("- Jugar un partido de futbol.\n")
    file.write("- Ir al cine con mi esposa.\n")
    file.write("- Prepara equipaje para salir de viaje.\n")

# Lectura de Archivo de Texto
# Abrimos el archivo my_notes.txt en modo de lectura 
with open('my_notes.txt', 'r') as file:
    # Leemos el contenido del archivo línea por línea
    for line in file.readlines():
        # Mostramos en la consola cada línea leída
        print(line.strip())  # Utilizamos strip() para eliminar los caracteres de nueva línea al final de cada línea

# Cierre de Archivos
# No es necesario cerrar explícitamente el archivo debido al uso del contexto 'with',
# que se encarga de cerrar el archivo automáticamente una vez que se sale del bloque 'with'