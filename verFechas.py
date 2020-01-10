import csv


def extractFechasScreen(file):
    f = open(file, encoding="utf8")

    lineas = f.readlines()

    f.close()

    fechas = lineas[12:20]

    for i in range(0, len(fechas)):
        fechas[i] = fechas[i][4:14]

    return fechas


def extractCSV(file, nHC):
    fechasToExtract = []
    with open(file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')        
        for row in csv_reader:
            if row[0] == nHC:
                tmp = row[1][0:4]+ '/' +row[1][4:6] + '/' + row[1][6:8]
                fechasToExtract.append(tmp)
    #print(fechasToExtract)
    return fechasToExtract



def cargarHC(lista, file):
    with open(file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')        
        for row in csv_reader:
            lista.append(row[0])
        
        lista = list(dict.fromkeys(lista))
    #print(lista)
    return lista