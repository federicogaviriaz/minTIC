diccionario_de_prueba = {
    'id_cliente': 2,
    'nombre': "Gloria Suarez",
    'edad': 4,
    'primer_ingreso': True
}


def cliente(informacion: dict) -> dict:
    nuevoDict = {
        'nombre': informacion['nombre'],
        'edad': informacion['edad'],
        'atraccion': 'default',
        'apto': True,
        'primer_ingreso': informacion['primer_ingreso'],
        'total_boleta': 000
    }

    if nuevoDict['edad'] > 18:
        nuevoDict['total_boleta'] = 20000
        nuevoDict['atraccion'] = "X-Treme"
    elif nuevoDict['edad'] >= 15:
        nuevoDict['total_boleta'] = 5000
        nuevoDict['atraccion'] = "Carros chochones"
    elif nuevoDict['edad'] >= 7:
        nuevoDict['total_boleta'] = 10000
        nuevoDict['atraccion'] = "Sillas voladoras"
    else:
        nuevoDict['total_boleta'] = "N/A"
        nuevoDict['atraccion'] = "N/A"
        nuevoDict['apto'] = False
    if nuevoDict['primer_ingreso'] == True and nuevoDict['total_boleta'] != "N/A":
        if nuevoDict['atraccion'] == "X-Treme" or nuevoDict['atraccion'] == "Sillas voladoras":
            nuevoDict['total_boleta'] = nuevoDict['total_boleta'] - \
                (nuevoDict['total_boleta']*0.05)
        else:
            nuevoDict['total_boleta'] = nuevoDict['total_boleta'] - \
                (nuevoDict['total_boleta']*0.07)
    return nuevoDict


print(cliente(diccionario_de_prueba))
