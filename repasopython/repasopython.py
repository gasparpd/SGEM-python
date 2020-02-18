text_file = open('matriz.txt')
filas = text_file.readline()
columnas = text_file.readline()
print (filas)
print (columnas)
# Creates a list containing 5 lists, each of 8 items, all set to 0
Matrix = [[0 for x in range(columnas)] for y in range(filas)]
